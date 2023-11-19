# admin.py
from django.contrib import admin
from MenuItem.models import MenuItem

from Shop.models import Vendor


def apply_vendor_filter(qs, user):
    """廠商只能看該資訊"""
    if not user.is_superuser:
        try:
            vendor = Vendor.objects.get(name=user.first_name)
            qs = qs.filter(name=vendor)
        except Vendor.DoesNotExist:
            # TODO: 需要做報錯！！！
            pass
    return qs


def apply_key_is_vendor_filter(qs, user):
    """廠商只能看該資訊"""
    if not user.is_superuser:
        try:
            vendor = Vendor.objects.get(name=user.first_name)
            qs = qs.filter(vendor=vendor)
        except Vendor.DoesNotExist:
            # TODO: 需要做報錯！！！
            pass
    return qs


def apply_menu_item_filter(qs, user):
    """廠商只能看該資訊"""
    if not user.is_superuser:
        try:
            qs = qs.filter(menu_item__vendor__name=user.first_name)
        except Exception as e:
            print(e)
            pass
    return qs


class BaseVendorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return apply_vendor_filter(qs, request.user)


class BaseVendorKeyAdmin(admin.ModelAdmin):
    """key 是 vendor使用"""

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return apply_key_is_vendor_filter(qs, request.user)


class BaseMenuItemAdmin(admin.ModelAdmin):
    """"""

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return apply_menu_item_filter(qs, request.user)
