from rest_framework import serializers

from ..entities.Source import Source, SourceItem
from ..entities.Condition import Condition
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..mixins.NestedSerializing import NestedSerializer


class SourceItemSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = SourceItem
        fields = ('id', 'action', 'condition', 'choice', 'token', 'source', 'cost', 'amount', 'restricted', 'allowed')

    def nested_entities(self):
        return [
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'restricted', 'model': Condition, 'm2m': True},
            {'name': 'allowed', 'model': Condition, 'm2m': True},
        ]


class SourceSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)
    items = SourceItemSerializer(many=True)

    class Meta:
        model = Source
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'mode', 'pick', 'items')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(SourceSerializer, self).to_internal_value(data)
        return value

    def nested_entities(self):
        return [
            {'name': 'items', 'model': Source, 'm2m': False, 'serializer': SourceItemSerializer},
        ]
