from rest_framework import serializers

from ..entities.Team import Team
from ..entities.Condition import Condition
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'settings', 'model': Condition, 'm2m': True}
])
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
