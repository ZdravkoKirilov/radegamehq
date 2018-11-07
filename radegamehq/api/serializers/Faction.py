from rest_framework import serializers

from ..entities.Faction import Faction
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..entities.Pool import Pool
from ..mixins.NestedSerializing import NestedSerializer
from ..entities.Stage import Stage


class FactionSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Faction
        fields = (
            'id', 'name', 'description', 'keywords', 'image', 'game', 'type', 'income', 'boards', 'effect_pool')

    def nested_entities(self):
        return [
            {'name': 'effect_pool', 'model': Pool, 'm2m': True},
            {'name': 'boards', 'model': Stage, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(FactionSerializer, self).to_internal_value(data)
        return value
