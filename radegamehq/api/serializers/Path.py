from rest_framework import serializers

from ..entities.Path import Path
from ..entities.Condition import Condition
from ..entities.Source import Source

from ..mixins.NestedSerializing import NestedSerializer
from .custom_serializers import Base64ImageField
from ..helpers.image_sanitize import sanitize_image


class MapPathSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Path
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'risk', 'model': Source, 'm2m': True},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        return super(MapPathSerializer, self).to_internal_value(data)
