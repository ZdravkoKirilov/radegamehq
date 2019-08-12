from rest_framework import serializers

from ..entities.Round import Round
from ..entities.Phase import Phase
from ..entities.Condition import Condition
from ..mixins.NestedSerializing import NestedSerializer


class RoundSerializer(NestedSerializer, serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'condition', 'model': Condition, 'm2m': True},
            {'name': 'phases', 'model': Phase, 'm2m': True}
        ]
