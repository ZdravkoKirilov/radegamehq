from rest_framework import serializers

from ..entities.Location import Location
from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image
from ..entities.Stack import Stack


class MapLocationSerializer(NestedSerializer, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'game', 'stage', 'field', 'token', 'width', 'height', 'y', 'x',)

    def nested_entities(self):
        return [
            {'name': 'allowed', 'model': Stack, 'm2m': True},
            {'name': 'restricted', 'model': Stack, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(MapLocationSerializer, self).to_internal_value(data)
        return value
