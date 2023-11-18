from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin import AdminSite

from MenuItem.models import ExtraOption, MenuItem, MenuItemCategory, MenuStatus, RequiredOption
from Shop.models import Vendor


# =================================================================

@admin.register(MenuItemCategory)
class MenuItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'name')
    list_filter = ('vendor',)  # 在管理员页面上添加供应商过滤器
    search_fields = ('vendor',)
    list_per_page = 30
    list_max_show_all = 200


@admin.register(MenuStatus)
class MenuStatusAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'remaining_quantity', 'is_available')
    list_filter = ('menu_item',)  # 使用外键关联的供应商进行过滤
    search_fields = ('menu_item__vendor__name',)  # 允许通过供应商名称搜索

    def vendor(self, obj):
        return obj.menu_item.vendor.name

    vendor.short_description = '廠商'

    # 顯示10個物件
    list_per_page = 10
    # default
    list_max_show_all = 200


@admin.register(ExtraOption)
class ExtraOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)

    list_filter = ('vendor__name',)  # 注意這裡的修改

    search_fields = ('vendor__name',)

    def category__name(self, obj):
        return obj.category.name

    def category__vendor_name(self, obj):
        return obj.category.vendor.name

    category__name.short_description = 'Category Name'
    category__vendor_name.short_description = 'Vendor Name'

    list_filter = ('vendor__name',)  # 注意這裡的修改

    search_fields = ('vendor__name',)    # 顯示10個物件
    list_per_page = 30
    # default
    list_max_show_all = 200


@admin.register(RequiredOption)
class ExtraOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)

    list_filter = ('vendor__name',)  # 注意這裡的修改

    search_fields = ('vendor__name',)

    def category__name(self, obj):
        return obj.category.name

    def category__vendor_name(self, obj):
        return obj.category.vendor.name

    category__name.short_description = 'Category Name'
    category__vendor_name.short_description = 'Vendor Name'

    list_filter = ('vendor',)
    # 顯示10個物件
    list_per_page = 30
    # default
    list_max_show_all = 200


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_img_url_preview',
                    'display_categories', 'extra_options', 'required_option_display', 'price', 'display_vendor')
    list_filter = ('vendor__name',)  # 注意這裡的修改

    search_fields = ('vendor__name',)

    # 顯示五個物件
    list_per_page = 50

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    display_categories.short_description = '食物類別'

    def extra_options(self, obj):
        if obj.extra_option.exists():
            return ", ".join([extra_option.name for extra_option in obj.extra_option.all()])
        else:
            return "None"

    extra_options.short_description = '額外選項'

    def required_option_display(self, obj):
        return ", ".join([required_option.name for required_option in obj.required_option.all()])

    required_option_display.short_description = '必選選項'

    # required_option.short_description = '必選選項'

    def display_vendor(self, obj):
        return obj.vendor.name

    display_vendor.short_description = '供應商'

    def menu_img_url_preview(self, obj):
        if obj.menu_img_url.url:
            return mark_safe(f'<div style="border-radius: 20%; overflow: hidden; width: 100px; height: 100px;"><img src="{obj.menu_img_url.url}" style="width: 100%; height: 100%;" /></div>')
        else:
            return '<span style="color:red;">沒有圖片</span>'

    menu_img_url_preview.allow_tags = True
    menu_img_url_preview.short_description = '菜單預覽圖'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category":
            vendor_id = request.POST.get('vendor', None)
            if vendor_id:
                kwargs["queryset"] = MenuItemCategory.objects.filter(
                    vendor__id=vendor_id)
            else:
                kwargs["queryset"] = MenuItemCategory.objects.none()

        if db_field.name == "extra_option":
            vendor_id = request.POST.get('vendor', None)
            if vendor_id:
                kwargs["queryset"] = ExtraOption.objects.filter(
                    vendor__id=vendor_id)
            else:
                kwargs["queryset"] = ExtraOption.objects.none()

        if db_field.name == "required_option":
            vendor_id = request.POST.get('vendor', None)
            if vendor_id:
                kwargs["queryset"] = ExtraOption.objects.filter(
                    vendor__id=vendor_id)
            else:
                kwargs["queryset"] = ExtraOption.objects.none()

        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "vendor" and not request.user.is_superuser:
            kwargs["queryset"] = Vendor.objects.filter(
                id=request.user.vendor.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# =================================================================
admin.site.site_title = '菜單'
