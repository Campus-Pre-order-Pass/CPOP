from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("vendor", "customer", "order_time",
                    "take_time", "total_amount", "order_status")
    ordering = ("-take_time",)

    list_filter = ('vendor__name',)

    list_per_page = 20


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("menuItem", "quantity")

    list_filter = ('order__vendor__name',)

    list_per_page = 20
