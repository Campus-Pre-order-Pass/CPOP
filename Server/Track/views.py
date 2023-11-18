import datetime
import random
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from django.http import HttpRequest
from django.shortcuts import render
import logging

# chart
from chartjs.views.lines import BaseLineChartView

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes

# models
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.db.models import Sum, F, ExpressionWrapper, fields
from Track.models import DailyNewUsers, DailyOrders, DailySales, TotalOrders, TotalSales, TotalUsers, VisitsandPageViews
from backend.Shop.vendor import Vendor

# helpers
from helper.change import get_model_data, process_data
# from Shop.models.shop import Shop

# 获取今天的日期
TODAT = date.today()
months_ago = 3  # 获取三个月以前的数据


shop_ID_list = ["GUHf5vZMkJhfVzQlfTx1vv6Dwvj1", "CFrwnEMFl1dM1RfleSsmLXLmNbR2"]


@api_view(['GET'])
def init(request):
    # 获取开始日期和结束日期

    # 模拟每天的请求，创建记录
    current_date = TODAT
    end_date = 0
    while current_date > end_date:
        views_request = HttpRequest()
        views_request.method = 'GET'
        # 请注意，这里使用的是 shop_id，而不是 id
        random_count = random.randint(0, 1000)
        for shop_ID in shop_ID_list:
            v = Vendor.objects.get(uid=shop_ID)

            # 使用 increase_count 方法来增加计数
            # dailyViews
            # daily_new_users = DailyNewUsers.increase_count(
            #     v, current_date)
            # total_users = TotalUsers.increase_total_count(v, current_date)

            # order
            daily_new_users = DailyOrders.increase_count(
                v, current_date)
            total_users = TotalOrders.increase_total_count(v, current_date)

            # sales
            daily_new_users = DailySales.increase_money(
                v, random_count,  current_date)
            total_users = TotalSales.increase_total_money(
                v, random_count, current_date)

            # daily_new_users
            # daily_new_users(request=views_request, shop_id=shop_ID)
            VisitsandPageViews.increase_count(
                v, current_date)

        # 递减日期
        current_date -= timedelta(days=1)

    return Response(status=status.HTTP_201_CREATED)


def clear(request):
    # for shop_ID in shop_ID_list:

    #     v = Vendor.objects.get(uid=shop_ID)

    #     # 使用 increase_count 方法来增加计数
    #     # dailyViews
    #     daily_new_users = DailyNewUsers.objects.create(
    #         vendor=v, count=random_count, date=end_date)
    #     total_users = TotalUsers.increase_total_count(v, end_date)

    #     # order
    #     daily_new_users = DailyOrders.objects.create(
    #         vendor=v, count=random_count, date=end_date)
    #     total_users = TotalOrders.increase_total_count(v, end_date)

    #     daily_new_users = DailySales.increase_money(
    #         v, random_count,  end_date)
    #     total_users = TotalSales.increase_total_money(
    #         v, random_count, end_date)
    #     pass
    pass


# DailyViews =============================================================


@api_view(['GET'])
def daily_new_users(request, shop_id, today=None):

    if today is None:
        today = date.today()

    try:
        # 尝试获取今天的瀏覽次數记录，如果不存在则创建
        v = Vendor.objects.get(uid=shop_id)

        # 使用 increase_count 方法来增加计数
        # dailyViews
        daily_new_users = DailyNewUsers.increase_count(v, today)
        total_users = TotalUsers.increase_total_count(v, today)

        return Response(status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def order(request, shop_id):
    if today is None:
        today = date.today()
    try:
        v = Vendor.objects.get(uid=shop_id)

        # 使用 increase_count 方法来增加计数
        # dailyViews
        daily_new_users = DailyOrders.increase_count(v, today)
        total_users = TotalOrders.increase_total_count(v, today)

        return Response(status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def sales(request, shop_id, money):
    if today is None:
        today = date.today()
    try:
        v = Vendor.objects.get(uid=shop_id)

        # 使用 increase_count 方法来增加计数
        # dailyViews
        daily_new_users = DailySales.increase_money(v, money,  today)
        total_users = TotalSales.increase_total_money(v, money, today)

        return Response(status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def visit(request):
    pass


@api_view(['GET'])
def merchant(request, uid):
    try:
        v = Vendor.objects.get(uid=uid)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    # 获取当前月份
    current_month = datetime.datetime.now().month

    # 获取 Vendor 对象
    v = Vendor.objects.get(uid=uid)

    # 查询: 获取每日订单数据和总订单总数
    queryset = DailyOrders.objects.filter(vendor=v).annotate(
        truncated_date=TruncDay("date")
    ).values("truncated_date").annotate(
        daily_orders=Sum("count"),
        daily_sales=Sum("count"),
        # total_orders=Sum(
        #     'vendor__total_orders__count',
        #     filter=F('date__month') == current_month
        # )
    ).order_by("-truncated_date")

    # 计算 total_daily_orders 和 total_daily_sales
    total_daily_orders = sum(item["daily_orders"] for item in queryset)
    total_daily_sales = sum(item["daily_sales"] for item in queryset)

    # 构造 JSON 数据
    chart_data = [
        {
            "date": item["truncated_date"].isoformat(),
            "daily_orders": item["daily_orders"],
            "daily_sales": item["daily_sales"],
        }
        for item in queryset
    ]

    data_json = {
        "total_orders": total_daily_orders,
        "total_sales": total_daily_sales,
    }

    response_data = {
        "chart_data": chart_data,
        "data": data_json,
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def test(request):
    logger = logging.getLogger('LoggerName')
    logger.info('The info message')
    logger.warning('The warning message')
    logger.error('The error message')

    return Response("result", status=status.HTTP_200_OK)
