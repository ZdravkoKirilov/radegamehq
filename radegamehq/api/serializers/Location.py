from rest_framework import serializers

from ..entities.Location import Location
from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image
from ..entities.Stack import Stack
from ..entities.Token import Token
from .custom_serializers import Base64ImageField


class MapLocationSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Location
        fields = (
            'id', 'game', 'owner', 'name', 'description', 'image', 'keywords', 'field', 'tokens', 'width', 'height',
            'y', 'x', 'allowed', 'restricted')

    def nested_entities(self):
        return [
            {'name': 'allowed', 'model': Stack, 'm2m': True},
            {'name': 'restricted', 'model': Stack, 'm2m': True},
            {'name': 'tokens', 'model': Token, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(MapLocationSerializer, self).to_internal_value(data)
        return value
