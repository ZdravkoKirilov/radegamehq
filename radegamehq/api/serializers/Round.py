from rest_framework import serializers

from ..entities.Round import Round
from ..entities.Stack import Stack
from ..entities.Pool import Pool
from ..entities.Phase import Phase
from ..helpers.image_sanitize import sanitize_image
from ..mixins.NestedSerializing import NestedSerializer
from .custom_serializers import Base64ImageField


class RoundSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(use_url=True, allow_empty_file=True, allow_null=True)

    class Meta:
        model = Round
        fields = (
            'id', 'game', 'name', 'description', 'image', 'replay_count', 'stage', 'award', 'penalty',
            'condition', 'effect_pool', 'phases', 'phase_order')

    def nested_entities(self):
        return [
            {'name': 'condition', 'model': Stack, 'm2m': True},
            {'name': 'award', 'model': Stack, 'm2m': True},
            {'name': 'penalty', 'model': Stack, 'm2m': True},
            {'name': 'effect_pool', 'model': Pool, 'm2m': True},
            {'name': 'phases', 'model': Phase, 'm2m': True}
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(RoundSerializer, self).to_internal_value(data)
        return value
