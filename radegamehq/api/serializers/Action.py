from rest_framework import serializers

from ..entities.Action import ActionConfig, Action

from ..mixins.NestedSerializing import with_nesting


class ActionConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionConfig
        fields = '__all__'


@with_nesting([
    {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
])
class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)

    class Meta:
        model = Action
        fields = '__all__'
