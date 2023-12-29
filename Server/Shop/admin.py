from django.contrib import admin
from django.conf import settings
from Shop.models import CurrentState, DayOfWeek, Vendor, Promotion
from helper.admin.vendor_class_base import BaseVendorAdmin, BaseVendorKeyAdmin


# =================================================================

@admin.register(CurrentState)
class CurrentStateAdmin(BaseVendorKeyAdmin):
    list_display = ('vendor', 'current_number', 'is_start')
    list_filter = ('vendor__name',)

    search_fields = ('vendor__name',)
    list_per_page = 10


@admin.register(DayOfWeek)
class DayOfWeekAdmin(BaseVendorKeyAdmin):
    list_display = ('vendor', 'day', 'open_time', 'close_time')
    list_filter = ('vendor__name',)

    search_fields = ('vendor__name',)
    list_per_page = 10


@admin.register(Vendor)
class VendorAdmin(BaseVendorAdmin):
    list_display = ('name', 'principal', 'campus_name', 'contact')
    list_filter = ('name',)  # 注意這裡的修改

    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:  # 如果不是超級用戶
            if request.user.username == 'vendor':
                qs = qs.filter(name="水餃店")  # 假設 "水餃" 的 vendor id 是 1

        return qs
    # C
    list_per_page = 10

    # TODO: 改
    # admin.site.site_title = '我在浏览器标签后面'
    # admin.site.index_title = '我在浏览器标签前面'

    # readonly_fields = ["vendor_img_preview"]

    # def vendor_img_preview(self, obj):
    #     if obj.vendor_img_url:
    #         return mark_safe('<img src="{url}" width="500" height="auto" />'.format(
    #             url=obj.vendor_img_url.url,
    #             width=obj.vendor_img_url.width,
    #             height=obj.vendor_img_url.height,
    #         ))
    #     else:
    #         return "No Image"

    # vendor_img_preview.short_description = "Vendor Image Preview"


@admin.register(Promotion)
class PromotionAdmin(BaseVendorKeyAdmin):
    list_display = ('vendor', 'promotions', 'promotion_type', 'end_time')
    list_filter = ('vendor__name',)

    search_fields = ('vendor__name',)

    ordering = ('-created_at',)

    list_per_page = 20


# =============================================================================
admin.site.site_header = settings.SITEHEADER
# TODO: change
admin.site.site_title = '商店'
# admin.site.index_title = '商店'

# 在不同站点上注册模型
admin.register(Vendor, VendorAdmin)
admin.register(CurrentState, CurrentStateAdmin)
# admin.register(DayOfWeek, DayOfWeekAdmin)

# admin.register(Customer, CustomerAdmin)
# admin.register(MenuStatus, MenuStatusAdmin)

# admin.register(MenuItemCategory, MenuItemCategoryAdmin)
# admin.register(MenuItem, MenuItemAdmin)
