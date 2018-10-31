from rest_framework import serializers
from ..entities.Token import Token

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..entities.Stack import Stack
from ..entities.Pool import Pool
from ..mixins.NestedSerializing import NestedSerializer


class TokenSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True, allow_empty_file=True)

    class Meta:
        model = Token
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'start', 'effect_pool', 'restricted', 'allowed')

    def nested_entities(self):
        return [
            {'name': 'restricted', 'model': Stack, 'm2m': True},
            {'name': 'allowed', 'model': Stack, 'm2m': True},
            {'name': 'effect_pool', 'model': Pool, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(TokenSerializer, self).to_internal_value(data)
        return value
