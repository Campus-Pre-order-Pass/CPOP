from rest_framework import serializers

from Shop.models import CurrentState, Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ["created_at", "principal"]


class CurrentStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrentState
        exclude = ["id", "vendor"]
        # fields = '__all__'
