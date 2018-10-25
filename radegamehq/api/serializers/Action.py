from rest_framework import serializers

from .custom_serializers import Base64ImageField
from ..entities.Action import ActionConfig, Action
from api.mixins.NestedSerializing import NestedSerializer
from api.entities.Stack import Stack
from api.helpers.image_sanitize import sanitize_image

class ActionConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionConfig
        fields = ('id', 'type', 'target', 'condition', 'choice', 'faction', 'keywords', 'amount', 'resource')


class ActionSerializer(NestedSerializer, serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Action
        fields = ('id', 'name', 'description', 'keywords', 'image', 'game', 'configs', 'cost', 'condition',
                  'restriction', 'mode')

    def nested_entities(self):
        return [
            {'name': 'configs', 'model': ActionConfig, 'm2m': False, 'serializer': ActionConfigSerializer},
            {'name': 'cost', 'model': Stack, 'm2m': True},
            {'name': 'condition', 'model': Stack, 'm2m': True},
            {'name': 'restriction', 'model': Stack, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ActionSerializer, self).to_internal_value(data)
        return value

    # @transaction.atomic
    # def create(self, validated_data):
    #     action = self.update_all_items(validated_data, Action)
    #     return action
    #
    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     instance = self.update_all_items(validated_data, Action, instance)
    #     return instance
