from rest_framework import serializers

from ..entities.Faction import Faction
from ..entities.Slot import Slot
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'slots', 'model': Slot, 'm2m': True},
])
class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = '__all__'
