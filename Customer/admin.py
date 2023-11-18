from django.contrib import admin

from Customer.models import Customer


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10
    date_hierarchy = 'created_at'
