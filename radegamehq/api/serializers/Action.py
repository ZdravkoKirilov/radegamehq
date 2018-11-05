from rest_framework import serializers

from .custom_serializers import Base64ImageField
from ..entities.Action import ActionConfig, Action
from api.mixins.NestedSerializing import NestedSerializer
from api.entities.Stack import Stack
from api.helpers.image_sanitize import sanitize_image


class ActionConfigSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ActionConfig
        fields = (
            'id', 'type', 'target', 'condition', 'choice', 'token', 'faction', 'keywords', 'resource', 'amount',
            'max_amount', 'min_amount', 'value')


class ActionSerializer(NestedSerializer, serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Action
        fields = ('id', 'name', 'description', 'keywords', 'image', 'game', 'configs', 'cost', 'condition',
                  'restricted', 'allowed', 'mode', 'limit')

    def nested_entities(self):
        return [
            {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
            {'name': 'cost', 'model': Stack, 'm2m': True},
            {'name': 'condition', 'model': Stack, 'm2m': True},
            {'name': 'restricted', 'model': Stack, 'm2m': True},
            {'name': 'allowed', 'model': Stack, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ActionSerializer, self).to_internal_value(data)
        return value
