from rest_framework import serializers

from MenuItem.models import ExtraOption, MenuItem, RequiredOption, MenuStatus

# models


class RequiredOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredOption
        exclude = ["vendor"]


class MenuStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuStatus
        exclude = ["id", "menu_item", "date"]


class ExtraOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraOption
        exclude = ["vendor"]


class MenuItemRequiredOptionSerializer(serializers.ModelSerializer):
    required_option = RequiredOptionSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ["required_option"]


class MenuItemExtraOptionSerializer(serializers.ModelSerializer):
    extra_option = ExtraOptionSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ["extra_option"]


class MenuItemSerializer(serializers.ModelSerializer):
    # 使用 SlugRelatedField 做關聯
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    # 關聯
    # extra_option = ExtraOptionSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        exclude = ["created_at", "vendor", "extra_option", "required_option"]
