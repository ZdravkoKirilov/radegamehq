from rest_framework import serializers

from ..entities.Team import Team
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..entities.Pool import Pool
from ..mixins.NestedSerializing import NestedSerializer


class TeamSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Team
        fields = (
            'id', 'name', 'description', 'keywords', 'image', 'game', 'min_players', 'max_players', 'effect_pool')

    def nested_entities(self):
        return [
            {'name': 'effect_pool', 'model': Pool, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(TeamSerializer, self).to_internal_value(data)
        return value