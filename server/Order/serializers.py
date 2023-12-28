from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["vendor", "customer", "created_at",
                   "confirmation_hash", "order_status"]


# class CurrentStateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Order
#         exclude = ["id", "vendor"]
#         # fields = '__all__'
