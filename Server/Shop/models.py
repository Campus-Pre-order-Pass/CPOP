from django.db import models
from django.conf import settings
import datetime
from datetime import date
from faker import Faker


# BaseStatusModel
from helper.tool.base_models import BaseStatusModel


fake = Faker()


class Vendor(models.Model):
    CAMPUS_CHOICES = settings.CAMPUS_CHOICES

    # 廠商名稱
    name = models.CharField(max_length=255, verbose_name="廠商名稱")

    # 負責人
    principal = models.CharField(max_length=255, verbose_name="負責人")

    # 電子郵件
    email = models.CharField(max_length=255, verbose_name="電子郵件")

    # 聯絡電話
    contact = models.CharField(max_length=15, verbose_name="聯絡電話")

    # 校區名稱
    campus_name = models.CharField(
        max_length=255, choices=CAMPUS_CHOICES, verbose_name="校區名稱")

    # menu_item_categories = models.ManyToManyField(
    #     MenuItemCategory, related_name='vendors')

    # 營業時間

    # day_of_week = models.ManyToManyField(
    #     "DayOfWeek", verbose_name="星期"
    # )

    # 廠商圖片URL
    vendor_img_url = models.ImageField(
        upload_to='vendor_images/', blank=True, null=True, verbose_name="廠商圖片URL")

    # 其他資訊
    desc = models.TextField(blank=True, null=True, verbose_name="其他資訊")

    # TODO: 要把促銷刪除獨立出來
    promotions = models.TextField(blank=True, null=True, verbose_name="促銷信息")

    # 商店連結URL
    shop_url = models.URLField(blank=True, null=True, verbose_name="商店連結URL")

    # Instagram連結URL
    ig_url = models.URLField(blank=True, null=True,
                             verbose_name="Instagram連結URL")

    # Facebook連結URL
    fd_url = models.URLField(blank=True, null=True,
                             verbose_name="Facebook連結URL")

    # 預訂數量
    preorder_qty = models.IntegerField(
        blank=True, null=True, verbose_name="預訂數量")

    # 創建時間
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "廠商"
        verbose_name_plural = "廠商"

    def __str__(self):
        return self.name

    @classmethod
    def get_vendor(cls, vendor_id: int):
        return cls.objects.get(id=vendor_id)


class DayOfWeek(models.Model):
    DAYS_OF_WEEK = (
        (1, '星期一'),
        (2, '星期二'),
        (3, '星期三'),
        (4, '星期四'),
        (5, '星期五'),
    )

    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='day_of_week', verbose_name="廠商")
    day = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name="星期")

    open_time = models.TimeField(default="08:00", verbose_name="營業時間")
    close_time = models.TimeField(default="17:00", verbose_name="關閉時間")

    rest_open_time = models.TimeField(
        default="15:00", verbose_name="休息開始時間"
    )
    rest_close_time = models.TimeField(
        default="17:00", verbose_name="休息結束時間"
    )

    class Meta:
        verbose_name = "廠商時間"
        verbose_name_plural = "廠商時間"

    def __str__(self):
        return f"{self.get_day_display()} - {self.open_time} to {self.close_time}"


SHOPPING_TYPES = [
    ('online', '線上購物'),
    ('physical', '實體購物'),
]


class CurrentState(BaseStatusModel):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='current_state', verbose_name="供應商")

    shopping_type = models.CharField(
        max_length=10, choices=SHOPPING_TYPES, default='online', verbose_name="購物類型")

    date = models.DateField(default=date.today, verbose_name="日期")

    current_number = models.IntegerField(default=0, verbose_name="當前號碼")

    wait_number = models.IntegerField(default=0, verbose_name="等待號碼")

    is_start = models.BooleanField(default=False, verbose_name="是否開業")

    is_delivery_available = models.BooleanField(
        default=False, verbose_name="是否提供外送")

    class Meta:
        unique_together = ['vendor', 'date']  # 确保每个厂商每天只有一条记录
        verbose_name = "商店狀態"
        verbose_name_plural = "商店狀態"

    def __str__(self):
        return f"Current State for {self.current_number}"


NEW_RELEASE = 'new_release'
NEW_OFFER = 'new_offer'
NEW_DISCOUNT = 'new_discount'

PROMOTION_TYPE_CHOICES = [
    (NEW_RELEASE, '新上市'),
    (NEW_OFFER, '新優惠'),
    (NEW_DISCOUNT, '新折扣'),
]


class Promotion(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='promotion', verbose_name="供應商")

    promotions = models.TextField(blank=True, null=True, verbose_name="促銷信息")

    is_show_promotion_price = models.BooleanField(
        default=False, verbose_name="顯示促銷價格")

    promotion_price = models.DecimalField(max_digits=10, decimal_places=2)

    promotion_image = models.ImageField(
        upload_to='promotion_images/', blank=True, null=True, verbose_name="促銷照片")

    promotion_type = models.CharField(
        max_length=50, choices=PROMOTION_TYPE_CHOICES, null=True, verbose_name="促銷類型")

    max_purchase_count = models.PositiveIntegerField(
        verbose_name="最大購買人數", default=30)

    simultaneous_purchase_limit = models.PositiveIntegerField(
        verbose_name="同時間購買人數限制", default=5)

    start_time = models.DateTimeField(verbose_name="促銷開始時間")

    end_time = models.DateTimeField(verbose_name="促銷結束時間")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "廠商促銷"
        verbose_name_plural = "促銷"

    def __str__(self):
        return f"{self.vendor.name}促銷: {self.promotions} {self.promotion_price}"


class VendorDailyMetrics(BaseStatusModel):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, verbose_name="廠商")

    date = models.DateField(verbose_name="日期")

    max_purchase_count = models.PositiveIntegerField(verbose_name="最大購買人數")
    current_purchase_count = models.PositiveIntegerField(
        verbose_name="現在購買人數", default=0)  # 預設為0

    simultaneous_purchase_limit = models.PositiveIntegerField(
        verbose_name="同時間購買人數限制")

    class Meta:
        unique_together = ['vendor', 'date']  # 确保每个厂商每天只有一条记录
        verbose_name = "廠商每日指標"
        verbose_name_plural = "每日指標"

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"

    def generate_fake_vendor_daily_metrics(vendor_id: int):
        vendor = Vendor.objects.get(id=vendor_id)
        date = fake.date_between(start_date="-30d", end_date="today")
        max_purchase_count = fake.random_int(min=1, max=100)
        simultaneous_purchase_limit = fake.random_int(min=1, max=50)
        current_purchase_count = fake.random_int(min=0, max=max_purchase_count)

        return VendorDailyMetrics(
            vendor=vendor,
            date=date,
            max_purchase_count=max_purchase_count,
            simultaneous_purchase_limit=simultaneous_purchase_limit,
            current_purchase_count=current_purchase_count
        )


class VendorSetting(models.Model):
    is_testing = models.BooleanField(default=False, verbose_name='是否正在測試')
    is_trial_run = models.BooleanField(default=False, verbose_name='是否試營運')
    is_active = models.BooleanField(default=False, verbose_name='是否活動')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')

    class Meta:
        verbose_name = "廠商設定"
        verbose_name_plural = "廠商設定"

    def __str__(self):
        return str(self.is_trial_run)
