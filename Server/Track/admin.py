# import json

# from django.contrib import admin
# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models import Count
# from django.db.models.functions import TruncDay
# from django.http import JsonResponse
# from django.urls import path
# from django.db.models import Sum, F

# # Register your models here.
# from Track.models import DailyNewUsers, DailyOrders, DailySales, TotalOrders, TotalSales, TotalUsers, VisitsandPageViews


# # chart_base_class
# from helper.admin.chart_base_class import ChartAdmin


# @admin.register(DailyNewUsers)
# class DailyNewUsersAdmin(ChartAdmin):
#     chart_title = "每日新增使用者"


# @admin.register(DailyOrders)
# class DailyOrdersAdmin(ChartAdmin):
#     chart_title = "每日訂單"


# @admin.register(DailySales)
# class DailySalesAdmin(ChartAdmin):
#     chart_title = "每日銷售"


# @admin.register(VisitsandPageViews)
# class VisitsandPageViewsAdmin(ChartAdmin):
#     chart_title = "每日使用人數"
