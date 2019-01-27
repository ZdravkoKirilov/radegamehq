from rest_framework import serializers

from ..entities.Action import ActionConfig, Action
from ..entities.Source import Source
from ..entities.Condition import Condition

from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image


class ActionConfigSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ActionConfig
        fields = '__all__'


class ActionSerializer(NestedSerializer, serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)

    class Meta:
        model = Action
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'condition', 'model': Condition, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'reveal_cost', 'model': Source, 'm2m': True},
        ]
