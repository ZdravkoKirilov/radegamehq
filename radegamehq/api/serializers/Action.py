from rest_framework import serializers

from ..entities.Action import ActionConfig, Action
from ..entities.Source import Source
from ..entities.Condition import Condition

from ..mixins.NestedSerializing import NestedSerializer, with_nesting


class ActionConfigSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ActionConfig
        fields = '__all__'


@with_nesting([
    {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
    {'name': 'cost', 'model': Source, 'm2m': True},
    {'name': 'condition', 'model': Condition, 'm2m': True},
    {'name': 'enable', 'model': Condition, 'm2m': True},
    {'name': 'disable', 'model': Condition, 'm2m': True},
    {'name': 'reveal_cost', 'model': Source, 'm2m': True},
    {'name': 'done', 'model': Source, 'm2m': True},
    {'name': 'undone', 'model': Source, 'm2m': True},
])
class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)

    class Meta:
        model = Action
        fields = '__all__'

    # def nested_entities(self):
    #     return [
    #         {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
    #         {'name': 'cost', 'model': Source, 'm2m': True},
    #         {'name': 'condition', 'model': Condition, 'm2m': True},
    #         {'name': 'enable', 'model': Condition, 'm2m': True},
    #         {'name': 'disable', 'model': Condition, 'm2m': True},
    #         {'name': 'reveal_cost', 'model': Source, 'm2m': True},
    #     ]
