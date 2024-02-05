from django.contrib import admin

from Customer.models import *


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10
    date_hierarchy = 'created_at'

@admin.register(CustomerGroupMembership)
class CustomerGroupMembershipAdmin(admin.ModelAdmin):
    pass