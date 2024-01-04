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


#  =================================================================


class RequiredOptionSerializer(serializers.Serializer):
    require_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class ExtraOptionSerializer(serializers.Serializer):
    extra_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class ItemSerializer(serializers.Serializer):
    menuItem_id = serializers.IntegerField()
    required_option = RequiredOptionSerializer(many=True)
    extra_option = ExtraOptionSerializer(many=True)
    quantity = serializers.IntegerField()
    order = serializers.IntegerField()
    menuItem = serializers.IntegerField()


class OrderRequestBodySerializer(serializers.Serializer):
    order = OrderSerializer()
    items = ItemSerializer(many=True)
