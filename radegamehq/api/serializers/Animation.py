from rest_framework import serializers

from ..entities.Animation import Animation, AnimationStep
from ..mixins.NestedSerializing import with_nesting


class AnimationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimationStep
        fields = '__all__'


@with_nesting([
    {'name': 'steps', 'model': AnimationStep, 'm2m': False, 'serializer': AnimationStepSerializer},
])
class AnimationSerializer(serializers.ModelSerializer):
    steps = AnimationStepSerializer(many=True)

    class Meta:
        model = Animation
        fields = '__all__'
