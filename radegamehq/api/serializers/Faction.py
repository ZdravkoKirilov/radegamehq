from rest_framework import serializers

from ..entities.Faction import Faction
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..entities.Condition import Condition
from ..entities.Setup import Setup
from ..mixins.NestedSerializing import NestedSerializer


class FactionSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Faction
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'settings', 'model': Condition, 'm2m': True},
            {'name': 'setups', 'model': Setup, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(FactionSerializer, self).to_internal_value(data)
        return value
