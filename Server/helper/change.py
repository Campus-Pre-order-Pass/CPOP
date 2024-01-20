from datetime import datetime, timedelta

from django.db import models


def get_model_data(model: models.Model, vendor, fields, months_within=None):
    queryset = model.objects.filter(vendor=vendor)

    if months_within is not None:
        target_date = datetime.now() - timedelta(days=months_within * 30)
        queryset = queryset.filter(date__gte=target_date)

    data = queryset.values(*fields)
    return [list(item.values()) for item in data]


def process_data(data, fields):
    result = {}

    for field in fields:
        result[field] = []

    for item in data:
        for field, value in zip(fields, item):
            result[field].append(value)

    return result
