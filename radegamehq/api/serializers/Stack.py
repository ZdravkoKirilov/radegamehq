from rest_framework import serializers

from api.entities.Stack import EffectStack, StackItem
from api.helpers.image_sanitize import sanitize_image
from api.mixins.NestedSerializing import NestedSerializer
from .custom_serializers import Base64ImageField


class StackItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackItem
        fields = ('id', 'owner', 'action', 'condition', 'choice', 'relation')


class StackSerializer(serializers.ModelSerializer, NestedSerializer):
    image = Base64ImageField(max_length=None, use_url=True)
    items = StackItemSerializer(many=True)

    class Meta:
        model = EffectStack
        fields = ('id', 'game', 'name', 'description', 'image', 'keywords')

    def nested_entities(self):
        return [
            {'name': 'items', 'model': StackItem, 'm2m': False, 'serializer': StackItemSerializer},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(StackSerializer, self).to_internal_value(data)
        return value
