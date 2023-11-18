from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from Shop.models import Vendor


def upload_vendor_image(request, vendor_id):
    if request.method == 'POST':
        vendor = Vendor.objects.get(pk=vendor_id)
        image = request.FILES.get('image')  # 从表单中获取图像文件
        if image:
            vendor.vendor_img_url = image  # 将图像存储到模型的图像字段中
            vendor.save()
