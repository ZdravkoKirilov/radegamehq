from rest_framework import serializers

from ..entities.Slot import Slot
from ..entities.Condition import Condition
from ..mixins.NestedSerializing import NestedSerializer
from ..entities.Source import Source


class SlotSerializer(NestedSerializer, serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'enable', 'model': Condition, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'settings', 'model': Source, 'm2m': True},
            {'name': 'risk', 'model': Source, 'm2m': True},
        ]
