from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
import uuid
from django.db import models
from django.conf import settings
from datetime import date
from faker import Faker

# models
from Shop.models import Vendor

# helper
from helper.vaidate import validate_count
from helper.tool.base_models import BaseStatusModel
from helper.tool.tool import tool


fake = Faker()


class MenuItemCategory(models.Model):
    """
    每家店都有自己的食物类别（MenuItemCategory）。

    这个模型用于表示每家店可以自定义的食物类别，这些类别将用于其菜单项。
    """
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='menu_item_categories', verbose_name="廠商")

    # 类别的名称
    name = models.CharField(max_length=30, verbose_name="標籤名稱")

    class Meta:
        verbose_name = "標籤"
        verbose_name_plural = "標籤"

    def __str__(self):
        return self.name


class RequiredOption(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, verbose_name="廠商", null=True)
    name = models.CharField(max_length=100, verbose_name="名稱", default="必選選項")
    description = models.TextField(verbose_name="解釋", null=True, default="")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="價格")

    class Meta:
        verbose_name = "必選選項"
        verbose_name_plural = "必選選項"

    def __str__(self):
        return self.name


class ExtraOption(models.Model):
    """每個菜單分類的額外選選擇"""
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, verbose_name="廠商", null=True)

    name = models.CharField(max_length=100, verbose_name="名稱")
    description = models.TextField(verbose_name="解釋", null=True, default="")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="價格")

    class Meta:
        verbose_name = "額外選項"
        verbose_name_plural = "額外選項"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    # TYPE_CHOICES = [
    #     ('staples', '主食'),
    #     ('bento', '便當'),
    #     ('beverages', '飲料'),
    #     ('other', '其他'),
    #     ('noodles', '麵類'),
    # ]
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='menu_items', verbose_name="廠商")  # 所屬供應商
    category = models.ManyToManyField(MenuItemCategory, verbose_name="食物標籤")
    #
    extra_option = models.ManyToManyField(
        ExtraOption, verbose_name="額外選項")
    required_option = models.ManyToManyField(
        RequiredOption, verbose_name="必選選項")

    title = models.CharField(max_length=100, verbose_name="標題")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[validate_count], verbose_name="價格")
    unit = models.CharField(max_length=100, default="份", verbose_name="單位")
    hot = models.BooleanField(default=False, verbose_name="是否為熱門商品")
    menu_img_url = models.ImageField(
        upload_to='menu_images/', blank=True, null=True, verbose_name="照片")
    desc = models.TextField(blank=True, null=True, verbose_name="商品描述")
    promotions = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="促銷信息")
    daily_max_orders = models.IntegerField(default=20, verbose_name="訂購數量")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "菜單"
        verbose_name_plural = "菜單列表"

        constraints = [
            models.CheckConstraint(check=models.Q(
                price__gte=0), name='price_non_negative'),  # 價格非負數檢查
        ]

    def __str__(self):
        return self.title


class MenuStatus(BaseStatusModel):
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, verbose_name="菜單")  # 菜單項目關聯
    preorder_qty = models.IntegerField(
        blank=True, null=True, verbose_name="預訂數量")

    remaining_quantity = models.PositiveIntegerField(
        default=0, verbose_name="剩餘數量")

    is_available = models.BooleanField(
        default=True, verbose_name="是否可以供應")

    date = models.DateTimeField(default=timezone.now, verbose_name="日期")

    class Meta:
        unique_together = ['menu_item', 'date']

        verbose_name = "菜單狀態"
        verbose_name_plural = "菜單狀態"

    def __str__(self):
        return str(self.menu_item)

    # @classmethod
    # def get_today_status(cls, menu_item: MenuItem):
    #     status = cls.get_status_for_today(menu_item)
    #     return status
    @classmethod
    def get_today_status(cls, menu_item: MenuItem):
        # return cls.base_get_today_status(id=menu_id, related_models=MenuItem)
        try:
            status = cls.objects.get(
                menu_item=menu_item, date=date.today())
            return status
        except cls.DoesNotExist as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.get_today_status")
        except Exception as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.get_today_status")

    @classmethod
    def create_or_get_today_status(cls, menu_item_id: int, vendor_id: int):
        vendor = Vendor.get_vendor(vendor_id)
        menu_item = MenuItem.objects.get(id=menu_item_id)

        # Check if a status record for today and the menu item already exists
        existing_status = cls.objects.filter(
            menu_item=menu_item, date__date=tool.get_now_time_taipei()).first()
        if existing_status:
            # If it exists, you might want to update it or handle accordingly
            return existing_status

        # Create a new status record for today and the menu item
        new_status = cls.objects.create(
            menu_item=menu_item,
            remaining_quantity=0,  # Provide the default value as needed
            preorder_qty=vendor.preorder_qty,
            is_available=True,  # Provide the default value as needed
            date=tool.get_now_time_taipei(),  # Provide the default value as needed
        )

        return new_status

    @classmethod
    def generate_faker_status(cls, menu_id: int,  vendor_id: int):
        menu_item = MenuItem.objects.get(id=menu_id)
        vendor = Vendor.get_vendor(vendor_id)

        # Generate fake data for the MenuStatus fields
        remaining_quantity = fake.random_int(min=0, max=100)
        is_available = fake.boolean()

        # Create a new MenuStatus instance with the generated fake data
        menu_status = cls(
            menu_item=menu_item,
            remaining_quantity=remaining_quantity,
            preorder_qty=vendor.preorder_qty,
            is_available=is_available,
            date=timezone.now(),
        )

        return menu_status
