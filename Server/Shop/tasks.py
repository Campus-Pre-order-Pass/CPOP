from celery import shared_task, signals
from django.core.mail import send_mail
from datetime import date
import logging

# models
from Shop.models import CurrentState, Vendor, VendorDailyMetrics

# django
import django
from django.db import transaction

# helper
from helper.tool.function import printerTool
from helper.task.check import check_taiwan_weekend_decorator


logger = logging.getLogger('tasks')  # 创建名为 'tasks' 的日志记录器


@shared_task(ignore_result=True)
def test():
    print("ok")
    logger.info("Successfully created shop test.")


@shared_task(ignore_result=True)
@check_taiwan_weekend_decorator
def creat_shop_daily_instance():
    """創建shop狀態與每日指標"""
    try:
        # setup
        django.setup()

        vendors = Vendor.objects.all()
        with transaction.atomic():

            for vendor in vendors:
                # 检查是否已经存在今天的记录，如果存在则跳过
                if CurrentState.objects.filter(vendor=vendor, date=date.today()).exists():
                    continue

                daily_instance = CurrentState(
                    vendor=vendor,
                    date=date.today(),
                    current_number=0,  # default count
                    wait_number=0,
                    is_start=False,
                    is_delivery_available=False,
                )
                # printerTool.print_blue(daily_instance)
                daily_instance.save()

                vendor_daily_metrics = VendorDailyMetrics(
                    vendor=vendor,
                    date=date.today(),
                    max_purchase_count=vendor.preorder_qty,
                    simultaneous_purchase_limit=5
                )

                vendor_daily_metrics.save()
            logger.info("Successfully created shop daily instance.")

    except Exception as e:
        # 如果有任何异常，记录错误日志
        logger.error(f"Error creating shop daily instance: {e}", exc_info=True)
