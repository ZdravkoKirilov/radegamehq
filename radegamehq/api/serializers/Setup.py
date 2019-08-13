from rest_framework import serializers
from ..entities.Setup import Setup, RoundSlot
from ..mixins.NestedSerializing import with_nesting


class RoundSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoundSlot
        fields = '__all__'


@with_nesting([
    {'name': 'rounds', 'model': RoundSlot, 'm2m': False, 'serializer': RoundSlotSerializer},
])
class SetupSerializer(serializers.ModelSerializer):
    rounds = RoundSlotSerializer(many=True)

    class Meta:
        model = Setup
        fields = '__all__'
