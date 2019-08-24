from rest_framework import serializers

from ..entities.Faction import Faction
from ..entities.Stage import Stage
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'stages', 'model': Stage, 'm2m': True},
])
class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = '__all__'
