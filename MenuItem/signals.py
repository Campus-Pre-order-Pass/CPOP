from django.db.models.signals import post_save
from django.dispatch import receiver
# models
from MenuItem.admin import MenuItemCategoryAdmin
from MenuItem.models import MenuItem, MenuStatus
from Shop.models import CurrentState
from Auth.views import VendorAPIView


@receiver(post_save, sender=MenuItem)
def create_menu_status(sender, instance, created, **kwargs):
    """
    当创建新的菜单项时创建关联的 MenuStatus 记录
    """
    if created:
        MenuStatus.objects.create(menu_item=instance)
