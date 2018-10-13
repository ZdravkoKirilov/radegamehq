from django.db import transaction
from rest_framework import serializers
from typing import Dict

from .custom_serializers import Base64ImageField
from ..helpers.image_sanitize import sanitize_image
from ..entities.Action import ActionConfig, Action


class ActionConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionConfig
        fields = ('id', 'type', 'target', 'quest', 'trivia', 'faction', 'keyword', 'amount', 'resource')


class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Action
        fields = ('id', 'name', 'description', 'keywords', 'mode', 'image', 'game', 'configs', 'cost')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ActionSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        configs = validated_data.pop('configs')
        cost = validated_data.pop('cost')

        activity = Action.objects.create(name=validated_data['name'],
                                         description=validated_data['description'],
                                         image=validated_data['image'],
                                         game=validated_data['game'],
                                         mode=validated_data['mode'],
                                         keywords=validated_data['keywords'])

        for item in configs:
            self.save_act_config(item, activity)
        for item in cost:
            self.save_act_cost(item, activity)

        return activity

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_configs = ActionConfig.objects.filter(activity=instance)
        configs = validated_data.pop('configs')
        config_ids = [item['id'] for item in configs if 'id' in item]

        try:
            existing_configs.exclude(pk__in=config_ids).delete()
        except ActionConfig.DoesNotExist:
            pass

        for item in configs:
            try:
                obj = ActionConfig.objects.get(pk=item['id'])
                self.save_act_config(item, instance, obj)
            except (KeyError, ActionConfig.DoesNotExist) as e:
                self.save_act_config(item, instance)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_act_config(cls, item: Dict[str, any], activity: Action, obj=None) -> ActionConfig:
        if obj is None:
            obj = ActionConfig(activity=activity, target=item['target'], type=item['type'], )

        obj.__dict__.update(**item)
        obj.save()
        return obj
