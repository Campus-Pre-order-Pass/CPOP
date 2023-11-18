from django.db import models
from django.conf import settings


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


class CurrentState(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='current_state', verbose_name="供應商")
    current_number = models.IntegerField(default=0, verbose_name="當前號碼")
    wait_number = models.IntegerField(default=0, verbose_name="等待號碼")
    is_start = models.BooleanField(default=False, verbose_name="是否開業")
    is_delivery_available = models.BooleanField(
        default=False, verbose_name="是否提供外送")

    class Meta:
        verbose_name = "商店狀態"
        verbose_name_plural = "商店狀態"

    def __str__(self):
        return f"Current State for {self.current_number}"
