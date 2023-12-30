# models
from django.db import transaction
from MenuItem.models import MenuStatus, MenuItem

from celery import shared_task, signals
from django.core.mail import send_mail
from datetime import date
import logging

# django
import django


logger = logging.getLogger('tasks')
logger.setLevel(logging.DEBUG)


@shared_task(ignore_result=True)
def create_daily_menu_status_models():
    """Create daily menu status models"""
    try:
        with transaction.atomic():
            django.setup()

            # run

            menu_items = MenuItem.objects.all()
            menu_statuses = [
                MenuStatus(
                    menu_item=item,
                    remaining_quantity=item.remaining_quantity,
                    date=date.today()
                ) for item in menu_items
            ]

            MenuStatus.objects.bulk_create(menu_statuses)

            logger.info(
                f"Successfully created {len(menu_statuses)} menu status instances for today.")

    except Exception as e:
        # If there is any exception, record an error log
        logger.error(f"Error creating shop daily instance: {e}", exc_info=True)
