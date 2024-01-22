from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import requests
import json
import django
import sys
from django.conf import settings
from django.utils.decorators import method_decorator


# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.decorator.custom_ratelimit import custom_ratelimit
from django.views.decorators.cache import never_cache


# api
from drfa.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status

# models
from Shop.models import CurrentState, Vendor


# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .drf import DRF

BASE_URL = "https://cpop.api.iside.shop/"
PUT_URL = BASE_URL + "/v0/api/s/current/"


def zmMinFilterGray(src, r=7):
    """最小值滤波，r是滤波半径"""
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))


def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I * p, -1, (r, r))
    cov_Ip = m_Ip - m_I * m_p
    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I
    a = cov_Ip / (var_I + eps)
    b = m_p - a * m_I
    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))
    return m_a * I + m_b


def Defog(m, r, eps, w, maxV1):
    """计算大气光罩图V1和光照值A, V1 = 1-t/A"""
    V1 = np.min(m, 2)
    Dark_Channel = zmMinFilterGray(V1, 7)
    cv2.destroyAllWindows()

    # 􏰊看暗􏰈􏰉

    V1 = guidedfilter(V1, Dark_Channel, r, eps)

    # bins = 2000  # 如果你使用下面的直方图计算方法，可以不需要指定bins的值
    ht = np.histogram(V1.flatten(), bins=2000)  # 计算大气光照A的直方图

    # 计算累积分布函数
    d = np.cumsum(ht[0]) / float(V1.size)

    # 找到最大值的索引
    lmax = np.argmax(d > 0.999)

    # 计算大气光照A
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()

    V1 = np.minimum(V1 * w, maxV1)
    return V1, A


def deHaze(m, r=81, eps=0.001, w=0.95, maxV1=0.80, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxV1)  # 得到􏰇罩图􏰅和大气光照

    for k in range(3):
        Y[:, :, k] = (m[:, :, k] - Mask_img) / (1 - Mask_img / A)  # 颜色校正

    Y = np.clip(Y, 0, 1)

    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))  # gamma校正,􏰑认􏰒进行该

    return Y


def process_and_recognize_image(esp32_cam):
    PERCENTAGE = 0.4  # 紅色佔比範圍
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    CYAN = (0, 255, 255)
    DIGITSDICT = {
        (1, 1, 1, 1, 1, 1, 0): 0,
        (0, 1, 1, 0, 0, 0, 0): 1,
        (1, 1, 0, 1, 1, 0, 1): 2,
        (1, 1, 1, 1, 0, 0, 1): 3,
        (0, 1, 1, 0, 0, 1, 1): 4,
        (1, 0, 1, 1, 0, 1, 1): 5,
        (0, 0, 1, 1, 1, 1, 1): 6,
        (1, 1, 1, 0, 0, 1, 0): 7,
        (1, 1, 1, 1, 1, 1, 1): 8,
        (1, 1, 1, 1, 0, 1, 1): 9,
    }

    try:
        roi_color_n = deHaze(esp32_cam / 255.0) * 255

        roi_color_f = cv2.flip(roi_color_n, -1)  # 翻轉

        rows, cols, ch = roi_color_f.shape

        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
        pts2 = np.float32([[40, 60], [200, 50], [60, 210]])
        M = cv2.getAffineTransform(pts1, pts2)

        roi_color = cv2.warpAffine(roi_color_f, M, (cols, rows))  # 畫面歪斜

        contrast = 230  # 對比度增強因子
        brightness = -50  # 亮度增強因子
        contrast_image = roi_color * \
            (contrast / 127 + 1) - contrast + brightness
        contrast_image = np.clip(contrast_image, 0, 255)
        contrast_image = np.uint8(contrast_image)

        # roi = cv2.cvtColor(contrast_image, cv2.COLOR_BGR2GRAY)

        RATIO = contrast_image.shape[0] * 0.2

        roi = cv2.bilateralFilter(contrast_image, 5, 30, 60)

        trimmed = roi[int(RATIO):, int(RATIO): roi.shape[1] - int(RATIO)]
        roi_color = roi_color[int(RATIO):, int(
            RATIO): roi.shape[1] - int(RATIO)]

        h = roi.shape[0]
        ratio = int(h * 0.07)
        trimmed[-ratio:,] = 0
        trimmed[:, :ratio] = 0

        # 定義紅色的範圍
        lower_red = np.array([0, 0, 100])
        upper_red = np.array([255, 255, 255])

        # 在原始圖像上找到紅色的區域
        mask = cv2.inRange(trimmed, lower_red, upper_red)

        cnts, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        digits_cnts = []
        digits_cnts_small = []

        canvas = trimmed.copy()
        cv2.drawContours(canvas, cnts, -1, (255, 255, 255), 1)

        canvas = trimmed.copy()
        for cnt in cnts:
            (x, y, w, h) = cv2.boundingRect(cnt)
            if h > 160:  # 判斷是否為數字的高度(此觸需測試修改)
                digits_cnts += [cnt]
                rec = cv2.rectangle(
                    canvas, (x, y), (x + w, y + h), (0, 255, 255), 1)

                cv2.drawContours(
                    canvas, [cnt], 0, (0, 255, 255), 1
                )  # 注意這裡將 cnt 改為 [cnt]
            elif 60 < h <= 160:
                digits_cnts_small.append(cnt)

        # 新增合併處理的程式碼
        merged_rectangles = []  # 用來存儲合併後的矩形

        for i, cnt in enumerate(digits_cnts_small):
            current_x, current_y, current_w, current_h = cv2.boundingRect(cnt)

            for j in range(i):
                previous_x, previous_y, previous_w, previous_h = cv2.boundingRect(
                    digits_cnts_small[j]
                )

                # 判斷是否上下線接近
                length = min(
                    abs(current_y - previous_y - previous_h),
                    abs(previous_y - current_y - current_h),
                )
                print("length = ", length)
                if length < 10:  # (此處也需要測試修改)
                    # 合併兩個矩形
                    merged_x = min(current_x, previous_x)
                    merged_y = min(current_y, previous_y)
                    merged_w = (
                        max(current_x + current_w,
                            previous_x + previous_w) - merged_x
                    )
                    merged_h = current_h + previous_h + length

                    merged_rectangles.append(
                        (merged_x, merged_y, merged_w, merged_h))
                    # digits_cnts_small.append(cnt)

        # 在 canvas 上繪製合併後的矩形
        for rect in merged_rectangles:
            x, y, w, h = rect
            cv2.rectangle(canvas, (x, y), (x + w, y + h),
                          (0, 255, 0), 1)  # 修改顏色

        virtual_contours = []
        for rect in merged_rectangles:
            x, y, w, h = rect
            contour = np.array(
                [[x, y], [x + w, y], [x + w, y + h], [x, y + h]])
            virtual_contours.append(contour)

        # 現在，virtual_contours 中的每個元素都是一個模擬的輪廓，資料結構與 digits_cnts 類似。
        digits_cnts.extend(virtual_contours)

        print(f"No. of Digit Contours: {len(digits_cnts)}")

        # all_digits = digits_cnts_small + digits_cnts
        if len(digits_cnts) < 4 or len(digits_cnts) > 0:
            sorted_digits = sorted(
                digits_cnts, key=lambda cnt: cv2.boundingRect(cnt)[0]
            )

            canvas = trimmed.copy()

            for i, cnt in enumerate(sorted_digits):
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(
                    canvas, (x, y), (x + w, y + h), (0, 0, 255), 1
                )  # 使用紅色 (0, 0, 255)
                cv2.putText(
                    canvas, str(i), (x, y - 3), FONT, 1, (0, 0, 255), 1
                )  # 使用紅色 (0, 0, 255)

            digits = []
            canvas = roi_color.copy()
            for cnt in sorted_digits:
                (x, y, w, h) = cv2.boundingRect(cnt)
                roi = trimmed[y: y + h, x: x + w]
                print(f"W:{w}, H:{h}")
                # convenience units
                qW, qH = int(w * 0.3), int(h * 0.15)
                fractionH, halfH, fractionW = int(
                    h * 0.05), int(h * 0.5), int(w * 0.25)
                cH = int(h * 0.15)

                # seven segments in the order of wikipedia's illustration
                sevensegs = [
                    ((fractionW, 0), (w - fractionW, qH)),  # a (top bar)
                    ((w - qW, cH), (w, halfH - fractionH)),  # b (upper right)
                    ((w - qW, halfH + fractionH), (w, h - cH)),  # c (lower right)
                    ((fractionW, h - qH), (w - fractionW, h)),  # d (lower bar)
                    ((0, halfH + fractionH), (qW, h - qH)),  # e (lower left)
                    ((0, cH), (qW, halfH - fractionH)),  # f (upper left)
                    # ((0, halfH - fractionH), (w, halfH + fractionH)) # center
                    (
                        (0 + fractionW, halfH - fractionH),
                        (w - fractionW, halfH + fractionH),
                    ),  # center
                ]

                print(sevensegs)
                rec = roi.copy()
                for i in sevensegs:
                    rec = cv2.rectangle(rec, (i[0]), (i[1]), (255, 0, 0), 1)

                # initialize to off
                on = [0] * 7

                for i, ((p1x, p1y), (p2x, p2y)) in enumerate(sevensegs):
                    region = roi[p1y:p2y, p1x:p2x]
                    red_channel = region[:, :, 2]  # 取得紅色通道
                    _, binary = cv2.threshold(
                        red_channel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                    )
                    if np.sum(binary >= 200) > binary.size * PERCENTAGE:
                        on[i] = 1
                print(
                    f"{i}: Sum of 1: {np.sum(red_channel > 150)}, Sum of 0: {np.sum(red_channel <= 150)}, Shape: {region.shape}, Size: {region.size}"
                )
                print(f"State of ON: {on}")

                digit = -1
                if tuple(on) in DIGITSDICT.keys():
                    digit = DIGITSDICT[tuple(on)]
                    if digit == 8 and region.size < 1500 and w < 60:  # 1的情況
                        digit = 1
                if digit == -1:
                    {"status": "error", "message": "Invalid digit"}
                print(f"Digit is: {digit}")
                digits.append(str(digit))
                cv2.rectangle(canvas, (x, y), (x + w, y + h), CYAN, 1)
                cv2.putText(
                    canvas, str(digit), (x - 5, y +
                                         6), FONT, 1, (0, 255, 255), 1
                )

            print(f"Digits on the token are: {digits}")

            return {"status": "success", "digits": digits}
        else:
            return {"status": "error", "message": "Invalid digit"}
    except Exception as e:
        return {"status": "error", "message": "Hello, Error!"}


def save_model(vendor_id, current_number):
    if settings.TEST:
        try:
            CurrentState.get_today_status(vendor_id)
            return True
        except Vendor.DoesNotExist:
            return False
    try:
        v = Vendor.objects.get(id=vendor_id)
        # TODO: 需要修改
        c = CurrentState.get_today_status(vendor_id=v.id)

        c.current_number = current_number
        c.save()
        return True
    except Exception as e:
        print(e)
        return False


@handle_exceptions(CurrentState)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='PATCH'), name='patch')
@method_decorator(never_cache, name='patch')
class UploadImageAPIView(APIView):
    @swagger_auto_schema(
        operation_summary=DRF.upload_image["PATCH"]["operation_summary"],
        operation_description=DRF.upload_image["PATCH"]["operation_description"],
        consumes=DRF.upload_image["PATCH"]["consumes"],
        request_body=DRF.upload_image["PATCH"]["request_body"],
        responses=DRF.upload_image["PATCH"]["responses"],
    )
    def patch(slef, request):
        try:
            # 处理上传的图像数据
            image_data = request.FILES["image"].read()
            # image_data = request.POST.get("image")

            # 使用 cv2.imdecode() 从图像数据中读取图像
            nparr = np.frombuffer(image_data, np.uint8)
            roi_color = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            storeID = request.POST.get("storeID")

            # 调用图像处理函数
            result = process_and_recognize_image(roi_color)  # 圖片處理進入點
            # print("result:", result)

            digits = None
            digits = (
                int("".join(result["digits"])
                    ) if result["status"] == "success" else -1
            )
            data = {"current_number": digits}
            # print("data:", data)

            # TODO: check

            ok = save_model(storeID, digits)

            status = 'success' if ok else 'error'

            # 創建 JSON response 對象
            response_data = {"status": status, "digits": digits}
            return Response(response_data)
        except cv2.error as e:
            return Response({"status": "error", "message": str(e)})
