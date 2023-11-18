
from django.db import models

# models
from Customer.models import Customer
from Shop.models import Vendor


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', '已下單'),
        ('processing', '製作中'),
        ('completed', '完成'),
        ('canceled', '取消'),
    ]

    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='order_item', verbose_name="供應商")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='order_item', verbose_name="顧客")
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

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單列表"
