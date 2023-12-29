from django.db.models.signals import pre_delete
from django.dispatch import receiver

from Server import MenuItem
from Server.Order.models import OrderItem


@receiver(pre_delete, sender=Order)
def remove_order_related_data(sender, instance, **kwargs):
    # 在这里处理与 Order 关联的数据的删除逻辑
    # 例如，可以删除关联的 OrderItem 记录

    # 获取与 Order 关联的所有 OrderItem 记录
    related_order_items = OrderItem.objects.filter(order=instance)

    # 逐个删除 OrderItem 记录
    for order_item in related_order_items:
        order_item.delete()
