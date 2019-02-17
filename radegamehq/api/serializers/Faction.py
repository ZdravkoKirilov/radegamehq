from rest_framework import serializers

from ..entities.Faction import Faction
from ..entities.Condition import Condition
from ..entities.Game import Setup
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'settings', 'model': Condition, 'm2m': True},
    {'name': 'setups', 'model': Setup, 'm2m': True},
])
class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = '__all__'
