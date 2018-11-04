from rest_framework import serializers

from ..entities.Pool import Pool, PoolItem
from ..entities.Stack import Stack
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..mixins.NestedSerializing import NestedSerializer


class PoolItemSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = PoolItem
        fields = ('id', 'action', 'condition', 'choice', 'cost', 'quota', 'restricted', 'allowed')

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Stack, 'm2m': True},
            {'name': 'restricted', 'model': Stack, 'm2m': True},
            {'name': 'allowed', 'model': Stack, 'm2m': True},
        ]


class PoolSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)
    items = PoolItemSerializer(many=True)

    class Meta:
        model = Pool
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'mode', 'pick', 'quota', 'min_cap', 'max_cap',
            'random_cap', 'allow_same_pick', 'items')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(PoolSerializer, self).to_internal_value(data)
        return value

    def nested_entities(self):
        return [
            {'name': 'items', 'model': Pool, 'm2m': False, 'serializer': PoolItemSerializer},
        ]
