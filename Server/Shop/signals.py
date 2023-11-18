from django.db.models.signals import post_save
from django.dispatch import receiver
# models
from MenuItem.admin import MenuItemCategoryAdmin
from MenuItem.models import MenuItem, MenuItemCategory, MenuStatus
from Shop.models import CurrentState, Vendor


@receiver(post_save, sender=Vendor)
def initialize_menu_item_category(sender, instance, created, **kwargs):
    """在每次新增廠商的時候，會先把註冊基本標籤"""
    if created:
        TYPE_CHOICES = [
            ('staples', '主食'),
            ('bento', '便當'),
            ('beverages', '飲料'),
            ('other', '其他'),
            ('noodles', '麵類'),
        ]

        # 创建 MenuItemCategory 对象，每个对象代表一个类型
        for value, label in TYPE_CHOICES:
            MenuItemCategory.objects.create(vendor=instance, name=label)

        # 註冊餐廳狀態
        CurrentState.objects.create(vendor=instance)


@receiver(post_save, sender=MenuItem)
def create_menu_status(sender, instance, created, **kwargs):
    """
    当创建新的菜单项时创建关联的 MenuStatus 记录
    """
    if created:
        MenuStatus.objects.create(menu_item=instance)
