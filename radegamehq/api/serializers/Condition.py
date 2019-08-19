from rest_framework import serializers

from ..entities.Condition import Condition, ConditionFrame
from ..mixins.NestedSerializing import with_nesting


class ConditionFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionFrame
        fields = '__all__'


@with_nesting([
    {'name': 'frames', 'model': ConditionFrame, 'm2m': False, 'serializer': ConditionFrameSerializer}
])
class ConditionSerializer(serializers.ModelSerializer):
    frames = ConditionFrameSerializer(many=True)

    class Meta:
        model = Condition
        fields = '__all__'
