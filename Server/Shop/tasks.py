from celery import shared_task, signals
from django.core.mail import send_mail
from datetime import date
import logging

# models
from Shop.models import CurrentState, Vendor, VendorDailyMetrics

# django
import django


logger = logging.getLogger('tasks')  # 创建名为 'tasks' 的日志记录器


@shared_task(ignore_result=True)
def test():
    print("ok")
    logger.info("Successfully created shop test.")


@shared_task(ignore_result=True)
def creat_shop_daily_instance():
    """創建shop狀態與每日指標"""
    try:
        # setup
        django.setup()

        vendors = Vendor.objects.all()
        for vendor in vendors:
            # 检查是否已经存在今天的记录，如果存在则跳过
            if CurrentState.objects.filter(vendor=vendor, date=date.today()).exists():
                continue

            daily_instance = CurrentState(
                vendor=vendor,
                date=date.today(),
                current_number=0,  # 设置你的默认值
                wait_number=0,
                is_start=False,
                is_delivery_available=False,
            )
            daily_instance.save()

            vendor_daily_metrics = VendorDailyMetrics(
                vendor=vendor,
                date=date.today(),
                max_purchase_count=vendor.max_purchase_count,
                simultaneous_purchase_limit=vendor.simultaneous_purchase_limit
            )

            vendor_daily_metrics.save()
            logger.info("Successfully created shop daily instance.")

    except Exception as e:
        # 如果有任何异常，记录错误日志
        logger.error(f"Error creating shop daily instance: {e}", exc_info=True)
