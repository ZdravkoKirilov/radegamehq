import json

from django.db import transaction
from rest_framework import serializers

from ..entities.Activity import ActivityConfig, Activity
from ..entities.Resource import Resource
from ..entities.Quest import Quest
from ..entities.Trivia import Trivia
from ..entities.Faction import Faction

class ActivityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityConfig
        fields = ('id', 'type', 'target', 'amount', 'resource')
        read_only_fields = ('date_created', 'date_modified')


class ActivitySerializer(serializers.ModelSerializer):
    configs = ActivityConfigSerializer(many=True, source='config')

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'keywords', 'mode', 'image', 'game', 'configs')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(ActivitySerializer, self).to_internal_value(data)
        value['configs'] = json.loads(data['configs'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        configs = validated_data.pop('configs')

        activity = Activity.objects.create(name=validated_data['name'],
                                           description=validated_data['description'],
                                           image=validated_data['image'],
                                           game=validated_data['game'],
                                           mode=validated_data['mode'],
                                           keywords=validated_data['keywords'])

        for item in configs:
            self.save_act_config(item, activity)

        return activity

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_configs = ActivityConfig.objects.filter(activity=instance)
        configs = validated_data.pop('configs')
        config_ids = [item['id'] for item in configs if 'id' in item]

        try:
            existing_configs.exclude(pk__in=config_ids).delete()
        except ActivityConfig.DoesNotExist:
            pass

        for item in configs:
            try:
                obj = ActivityConfig.objects.get(pk=item['id'])
            except KeyError:
                obj = ActivityConfig.objects.create(activity=instance,
                                                    target=item['target'],
                                                    type=item['type'], )

            self.save_act_config(item, instance, obj)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_act_config(cls, item: ActivityConfig.__dict__, activity: Activity, obj=None) -> ActivityConfig:
        if obj is None:
            obj = ActivityConfig(activity=activity, target=item['target'], type=item['type'], )

        if 'resource' in item:
            resource = Resource.objects.get(pk=item['resource'])
            obj.resource = resource
        if 'quest' in item:
            quest = Quest.objects.get(pk=item['quest'])
            obj.quest = quest
        if 'trivia' in item:
            trivia = Trivia.objects.get(pk=item['trivia'])
            obj.trivia = trivia
        if 'faction' in item:
            faction = Faction.objects.get(pk=item['faction'])
            obj.faction = faction
        if 'keyword' in item:
            obj.keyword = item['keyword']
        if 'amount' in item:
            obj.amount = item['amount']

        obj.save()
        return obj
