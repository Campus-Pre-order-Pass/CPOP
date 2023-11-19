from django.contrib import admin

from CSP.models import CSPReport

# Register your models here.


@admin.register(CSPReport)
class CSPReportAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_max_show_all = 200
