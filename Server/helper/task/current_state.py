import logging
from datetime import date
from django.db import models

from Shop.models import CurrentState, Vendor
from MenuItem.models import MenuStatus, MenuItem

# 设置日志配置
logging.basicConfig(filename='logs/job.log', level=logging.INFO)

TODAY = date.today()


def update_current_state_action():
    vendors = Vendor.objects.all()

    for vendor in vendors:
        try:
            update_current_state(vendor)
            update_menu_state(vendor)
        except Exception as e:
            # 记录错误到日志
            logging.error(f"Error updating vendor {vendor.id}: {str(e)}")


def update_current_state(vendor: Vendor):
    try:
        current_state = CurrentState.objects.get(vendor=vendor)
        current_state.current_number = 0
        current_state.wait_number = 0
        current_state.is_start = False
        current_state.is_delivery_available = False
        current_state.save()
    except CurrentState.DoesNotExist:
        # Handle the case where CurrentState for this vendor does not exist
        pass


def update_menu_state(vendor: Vendor):
    try:
        menuItems = MenuItem.objects.filter(vendor=vendor)

        for menuItem in menuItems:
            try:
                menu_status = MenuStatus.objects.get(menu_item=menuItem)
                menu_status.remaining_quantity = menuItem.daily_max_orders
                menu_status.save()
            except MenuStatus.DoesNotExist:
                # Handle the case where MenuStatus for this menuItem does not exist
                pass
    except MenuItem.DoesNotExist:
        # Handle the case where no menu items are found for this vendor
        pass
