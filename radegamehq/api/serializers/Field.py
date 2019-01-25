from rest_framework import serializers

from ..entities.Field import Field
from ..entities.Source import Source

from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image


class FieldSerializer(NestedSerializer, serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'risk', 'model': Source, 'm2m': True},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(FieldSerializer, self).to_internal_value(data)
        return value
