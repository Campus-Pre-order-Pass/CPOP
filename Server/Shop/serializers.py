from rest_framework import serializers

from Shop.models import CurrentState, Vendor


from drf_yasg.utils import swagger_serializer_method


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ["created_at", "principal", "preorder_qty"]


class VendorSaveSerializer(serializers.ModelSerializer):
    """for save vendor models"""
    class Meta:
        model = Vendor
        exclude = ["created_at"]
        extra_kwargs = {
            # 'name': {'help_text': '廠商名稱'},
            # 'contact': {'help_text': ''},
            # 'preorder_qty': {'help_text': '每日最大承受數量'},
        }


class CurrentStateSerializer(serializers.ModelSerializer):
    # 舊版

    class Meta:
        model = CurrentState
        exclude = ["id", "vendor", "date"]
        # fields = '__all__'


# Response serializers
# class ResponseVendorSerializer(VendorSerializer):
#     @swagger_serializer_method(serializer_or_field=VendorSerializer)
#     def get_other_stuff(self, obj):
#         return VendorSerializer().data

#     @swagger_serializer_method(serializer_or_field=VendorSerializer(many=True))
#     def get_many_other_stuff(self, obj):
#         return VendorSerializer().data
