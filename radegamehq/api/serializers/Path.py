from rest_framework import serializers

from ..entities.Path import Path
from ..entities.Condition import Condition
from ..entities.Game import Setup

from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'enable', 'model': Condition, 'm2m': True},
    {'name': 'disable', 'model': Condition, 'm2m': True},
    {'name': 'setups', 'model': Setup, 'm2m': True}
])
class MapPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'
