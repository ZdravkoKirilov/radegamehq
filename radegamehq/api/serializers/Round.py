from rest_framework import serializers

from ..entities.Round import Round, PhaseSlot
from ..mixins.NestedSerializing import with_nesting


class PhaseSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhaseSlot
        fields = '__all__'


@with_nesting([
    {'name': 'phases', 'model': PhaseSlot, 'm2m': False, 'serializer': PhaseSlotSerializer},
])
class RoundSerializer(serializers.ModelSerializer):
    phases = PhaseSlotSerializer(many=True)

    class Meta:
        model = Round
        fields = '__all__'
