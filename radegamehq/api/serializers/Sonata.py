from rest_framework import serializers

from ..entities.Sonata import Sonata, SonataStep
from ..mixins.NestedSerializing import with_nesting


class SonataStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = SonataStep
        fields = '__all__'


@with_nesting([
    {'name': 'steps', 'model': SonataStep, 'm2m': False, 'serializer': SonataStepSerializer},
])
class SonataSerializer(serializers.ModelSerializer):
    steps = SonataStepSerializer(many=True)

    class Meta:
        model = Sonata
        fields = '__all__'
