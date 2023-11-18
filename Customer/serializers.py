from rest_framework import serializers

from Customer.models import Customer


class CustomerSerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["created_at"]
