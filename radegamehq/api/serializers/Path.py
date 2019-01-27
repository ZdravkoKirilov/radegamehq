from rest_framework import serializers

from ..entities.Path import Path
from ..entities.Condition import Condition
from ..entities.Source import Source

from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image


class MapPathSerializer(NestedSerializer, serializers.ModelSerializer):

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


