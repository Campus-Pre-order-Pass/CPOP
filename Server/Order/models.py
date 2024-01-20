
import hashlib
import secrets
from django.db import models
from django.utils import timezone

# models
from Customer.models import Customer
from Shop.models import Vendor
from MenuItem.models import ExtraOption, MenuItem, RequiredOption

ORDER_STATUS_CHOICES = [
    ('created', '創建'),
    ('pending', '已下單'),
    ('processing', '製作中'),
    ('completed', '完成'),
    ('canceled', '取消'),
    ('error', '錯誤'),
]


class Order(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='order_item', verbose_name="供應商")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='order_item', verbose_name="顧客")

    # order_items = models.ManyToManyField(
    #     OrderItem,  related_name='order_items', verbose_name="訂單項目")

    order_time = models.DateTimeField(auto_now_add=True, verbose_name="訂單日期")

    take_time = models.DateTimeField(verbose_name="取餐時間")

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="總金額")

    order_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        default='pending',  # 默认状态为'已下單'
        verbose_name="訂單狀態"
    )

    confirmation_hash = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="哈希加密")  # 使用 CharField 存储哈希值

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    # def save(self, *args, **kwargs):
    #     # 在保存订单前生成哈希值
    #     if not self.confirmation_hash:
    #         self.confirmation_hash = self.generate_confirmation_hash()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"

    def show(self):
        print(f"Order ID: {self.id}")
        print(f"Vendor: {self.vendor}")
        print(f"Customer: {self.customer}")
        print(f"Order Time: {self.order_time}")
        print(f"Take Time: {self.take_time}")
        print(f"Order Status: {self.order_status}")
        print(f"Created At: {self.created_at}")
        print(f"Confirmation Hash: {self.confirmation_hash}")

        print("")

        print(f"Total Amount: {self.total_amount}")

        print("")

        return "OK"

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單列表"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='訂單項目')

    menuItem = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name='menu_item', verbose_name="產品")

    quantity = models.PositiveIntegerField(default=1, verbose_name="數量")

    extra_option = models.ManyToManyField(
        ExtraOption, verbose_name="額外選項")

    required_option = models.ManyToManyField(
        RequiredOption, verbose_name="必選選項")

    def __str__(self):
        return f"{self.menuItem.title} - {self.quantity} 個"

    def show_order(self):
        extra_option_str = ", ".join(str(option)
                                     for option in self.extra_option.all())
        required_option_str = ", ".join(str(option)
                                        for option in self.required_option.all())

        return f"{self.menuItem.title} - {self.quantity} 個 (額外選項: {extra_option_str}, 必選選項: {required_option_str})"

    class Meta:
        verbose_name = "訂單產品"
        verbose_name_plural = "訂單產品列表"


class TransactionLog(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="使用者")
    action = models.CharField(max_length=255, verbose_name="交易動作")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="時間戳記")
    details = models.TextField(blank=True, null=True, verbose_name="交易詳情")

    def __str__(self):
        return f"{self.customer.name} - {self.action} - {self.timestamp}"

    class Meta:
        verbose_name = "交易日誌"
        verbose_name_plural = "交易日誌"
