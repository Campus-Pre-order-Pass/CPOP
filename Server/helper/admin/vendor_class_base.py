# admin.py
from django.contrib import admin

from Shop.models import Vendor


def apply_vendor_filter(qs, user):
    """廠商只能看該資訊"""
    if not user.is_superuser:
        try:
            vendor = Vendor.objects.get(name=user.username)
            qs = qs.filter(name=vendor.name)
        except Vendor.DoesNotExist:
            # TODO: 需要做報錯！！！
            pass
    return qs


class BaseVendorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return apply_vendor_filter(qs, request.user)
