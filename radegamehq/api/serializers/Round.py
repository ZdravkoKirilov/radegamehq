from rest_framework import serializers

from ..entities.Round import Round, Phase
from ..mixins.NestedSerializing import with_nesting


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'


@with_nesting([
    {'name': 'phases', 'model': Phase, 'm2m': False, 'serializer': PhaseSerializer},
])
class RoundSerializer(serializers.ModelSerializer):
    phases = PhaseSerializer(many=True)

    class Meta:
        model = Round
        fields = '__all__'
