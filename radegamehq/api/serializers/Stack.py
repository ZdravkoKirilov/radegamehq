from rest_framework import serializers

from api.entities.Stack import Stack, StackItem
from api.mixins.NestedSerializing import NestedSerializer
from .custom_serializers import Base64ImageField


class StackItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackItem
        fields = ('id', 'owner', 'action', 'condition', 'choice', 'relation')


class StackSerializer(serializers.ModelSerializer, NestedSerializer):
    items = StackItemSerializer(many=True, source='stack_owner')
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Stack
        fields = ('id', 'game', 'name', 'description', 'items', 'image', 'keywords')

    def nested_entities(self):
        return [
            {'name': 'items', 'model': StackItem, 'm2m': False, 'serializer': StackItemSerializer},
        ]
