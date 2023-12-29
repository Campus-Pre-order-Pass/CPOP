from rest_framework import serializers

from MenuItem.serializers import ExtraOptionSerializer, RequiredOptionSerializer

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["created_at"]


class OrderItemSerializer(serializers.ModelSerializer):
    required_option = RequiredOptionSerializer(many=True, read_only=True)
    extra_option = ExtraOptionSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        # exclude = ["vendor"]
        fields = '__all__'
