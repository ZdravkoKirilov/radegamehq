from rest_framework import serializers

from ..entities.Action import ActionConfig, Action
from ..entities.Condition import Condition

from ..mixins.NestedSerializing import with_nesting


class ActionConfigSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ActionConfig
        fields = '__all__'


@with_nesting([
    {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
    {'name': 'condition', 'model': Condition, 'm2m': True},
    {'name': 'enable', 'model': Condition, 'm2m': True},
    {'name': 'disable', 'model': Condition, 'm2m': True},
])
class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)

    class Meta:
        model = Action
        fields = '__all__'
