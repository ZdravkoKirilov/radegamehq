from rest_framework import serializers

from ..entities.Source import Source, SourceItem
from ..entities.Condition import Condition
from ..helpers.image_sanitize import sanitize_image
from ..mixins.NestedSerializing import NestedSerializer


class SourceItemSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = SourceItem
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'restricted', 'model': Condition, 'm2m': True},
            {'name': 'allowed', 'model': Condition, 'm2m': True},
        ]


class SourceSerializer(NestedSerializer, serializers.ModelSerializer):
    items = SourceItemSerializer(many=True)

    class Meta:
        model = Source
        fields = '__all__'

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(SourceSerializer, self).to_internal_value(data)
        return value

    def nested_entities(self):
        return [
            {'name': 'items', 'model': Source, 'm2m': False, 'serializer': SourceItemSerializer},
        ]
