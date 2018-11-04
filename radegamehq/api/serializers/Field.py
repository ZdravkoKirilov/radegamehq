from rest_framework import serializers

from ..entities.Field import Field
from ..entities.Stack import Stack
from ..entities.Pool import Pool
from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField


class FieldSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(use_url=True, allow_null=True, allow_empty_file=True)

    class Meta:
        model = Field
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'award', 'income', 'cost', 'penalty',
            'effect_pool')

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Stack, 'm2m': True},
            {'name': 'award', 'model': Stack, 'm2m': True},
            {'name': 'penalty', 'model': Stack, 'm2m': True},
            {'name': 'effect_pool', 'model': Pool, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(FieldSerializer, self).to_internal_value(data)
        return value
