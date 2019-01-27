from rest_framework import serializers

from ..entities.Faction import Faction
from ..helpers.image_sanitize import sanitize_image
from ..entities.Condition import Condition
from ..entities.Setup import Setup
from ..mixins.NestedSerializing import NestedSerializer


class FactionSerializer(NestedSerializer, serializers.ModelSerializer):

    class Meta:
        model = Faction
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'settings', 'model': Condition, 'm2m': True},
            {'name': 'setups', 'model': Setup, 'm2m': True},
        ]


