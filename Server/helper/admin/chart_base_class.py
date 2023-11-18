import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
from django.db.models import Sum, F


class ChartAdmin(admin.ModelAdmin):
    list_display = ("id", "count")
    ordering = ("-date",)

    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {
            "chart_data": as_json,
            "chart_title": self.chart_title,
        }
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        return extra_urls + urls

    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        queryset = self.model.objects.annotate(
            truncated_date=TruncDay("date")
        ).values("truncated_date").annotate(y=Sum("count")).order_by("-truncated_date")

        result = [
            {"date": item["truncated_date"].isoformat(), "y": item["y"]}
            for item in queryset
        ]

        return result
