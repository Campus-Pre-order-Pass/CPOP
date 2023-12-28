from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["created_at"]


# class CurrentStateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Order
#         exclude = ["id", "vendor"]
#         # fields = '__all__'
