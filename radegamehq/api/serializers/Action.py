from rest_framework import serializers

from ..entities.Action import ActionConfig, Action, ActionFrame
from ..mixins.NestedSerializing import with_nesting


class ActionFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionFrame
        fields = '__all__'


class ActionConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionConfig
        fields = '__all__'


@with_nesting([
    {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
    {'name': 'frames', 'model': ActionFrame, 'm2m': False, 'serializer': ActionFrameSerializer},
])
class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)

    class Meta:
        model = Action
        fields = '__all__'
