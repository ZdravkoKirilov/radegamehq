import json

from django.db import transaction
from rest_framework import serializers

from ..entities.Activity import ActivityConfig, Activity, ActivityCost
from ..entities.Resource import Resource
from ..entities.Quest import Quest
from ..entities.Trivia import Trivia
from ..entities.Faction import Faction


class ActivityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityConfig
        fields = ('id', 'type', 'target', 'quest', 'trivia', 'faction', 'keyword' 'amount', 'resource')
        read_only_fields = ('date_created', 'date_modified')


class ActivityCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityConfig
        fields = ('id', 'amount', 'resource', 'keyword')
        read_only_fields = ('date_created', 'date_modified')


class ActivitySerializer(serializers.ModelSerializer):
    configs = ActivityConfigSerializer(many=True, source='config')
    cost = ActivityCostSerializer(many=True, source='cost')

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'keywords', 'mode', 'image', 'game', 'configs', 'cost')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(ActivitySerializer, self).to_internal_value(data)
        value['configs'] = json.loads(data['configs'])
        value['cost'] = json.loads(data['cost'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        configs = validated_data.pop('configs')
        cost = validated_data.pop('cost')

        activity = Activity.objects.create(name=validated_data['name'],
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
        existing_configs = ActivityConfig.objects.filter(activity=instance)
        configs = validated_data.pop('configs')
        config_ids = [item['id'] for item in configs if 'id' in item]

        existing_costs = ActivityCost.objects.filter(activity=instance)
        costs = validated_data.pop('cost')
        cost_ids = [item['id'] for item in costs if 'id' in item]

        try:
            existing_configs.exclude(pk__in=config_ids).delete()
            existing_costs.exclude(pk__in=cost_ids).delete()
        except (ActivityConfig.DoesNotExist, ActivityCost.DoesNotExist) as e:
            pass

        for item in configs:
            try:
                obj = ActivityConfig.objects.get(pk=item['id'])
            except KeyError:
                obj = ActivityConfig.objects.create(activity=instance,
                                                    target=item['target'],
                                                    type=item['type'], )

            self.save_act_config(item, instance, obj)

        for item in costs:
            try:
                cost = ActivityCost.objects.get(pk=item['id'])
            except KeyError:
                cost = ActivityCost.objects.create(activity=instance)

            self.save_act_cost(item, instance, cost)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_act_config(cls, item: ActivityConfig, activity: Activity, obj=None) -> ActivityConfig:
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

    @classmethod
    def save_act_cost(cls, item: ActivityCost, activity: Activity, obj=None) -> ActivityCost:
        if obj is None:
            obj = ActivityCost(activity=activity)

        if 'resource' in item:
            resource = Resource.objects.get(pk=item['resource'])
            obj.resource = resource
        if 'keyword' in item:
            obj.keyword = item['keyword']
        if 'amount' in item:
            obj.amount = item['amount']

        obj.save()
        return obj
