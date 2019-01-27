from rest_framework import serializers

from ..entities.Team import Team
from ..helpers.image_sanitize import sanitize_image
from ..entities.Source import Source

from ..mixins.NestedSerializing import NestedSerializer


class TeamSerializer(NestedSerializer, serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'effect_pool', 'model': Source, 'm2m': True},
            {'name': 'income', 'model': Source, 'm2m': True}
        ]


