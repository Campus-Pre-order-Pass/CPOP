from rest_framework import serializers


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
    menu_item_id = serializers.IntegerField()
    required_option = RequiredOptionSerializer(many=True)
    extra_option = ExtraOptionSerializer(many=True)
    quantity = serializers.IntegerField()


class OrderItemSerializer(serializers.Serializer):
    menu_item_id = serializers.IntegerField()
    required_option_ids = serializers.ListSerializer(
        child=serializers.IntegerField())
    extra_option_ids = serializers.ListSerializer(
        child=serializers.IntegerField(), allow_empty=True
    )
    quantity = serializers.IntegerField()


class OrderRequestBodySerializer(serializers.Serializer):
    vendor_id = serializers.IntegerField()
    uid = serializers.CharField()
    take_time = serializers.DateTimeField()
    order_items = OrderItemSerializer(many=True)
