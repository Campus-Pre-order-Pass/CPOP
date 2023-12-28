
import hashlib
import secrets
from django.db import models

# models
from Customer.models import Customer
from Shop.models import Vendor
from MenuItem.models import ExtraOption, MenuItem, RequiredOption

ORDER_STATUS_CHOICES = [
    ('pending', '已下單'),
    ('processing', '製作中'),
    ('completed', '完成'),
    ('canceled', '取消'),
]


class OrderItem(models.Model):
    menuItem = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name='menu_item', verbose_name="產品")
    quantity = models.PositiveIntegerField(default=1, verbose_name="數量")
    extra_option = models.ManyToManyField(
        ExtraOption, verbose_name="額外選項")
    required_option = models.ManyToManyField(
        RequiredOption, verbose_name="必選選項")

    def __str__(self):
        return f"{self.menuItem.title} - {self.quantity} 個"

    class Meta:
        verbose_name = "訂單產品"
        verbose_name_plural = "訂單產品列表"


class Order(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='order_item', verbose_name="供應商")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='order_item', verbose_name="顧客")

    order_items = models.ManyToManyField(
        OrderItem, related_name='order_items', verbose_name="訂單項目")

    order_time = models.DateField(verbose_name="訂單日期")

    take_time = models.TimeField(verbose_name="取餐時間")

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="總金額")

    order_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        default='pending',  # 默认状态为'已下單'
        verbose_name="訂單狀態"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    confirmation_hash = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="哈希加密")  # 使用 CharField 存储哈希值

    # def save(self, *args, **kwargs):
    #     # 在保存订单前生成哈希值
    #     if not self.confirmation_hash:
    #         self.confirmation_hash = self.generate_confirmation_hash()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單列表"
