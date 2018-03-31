import json

from django.db import transaction
from rest_framework import serializers

from api.entities.Activity import Activity
from api.entities.Quest import Quest
from api.entities.Round import RoundQuest, RoundActivity, Round, RoundCondition


class RoundQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundQuest
        fields = ('id', 'quest')
        read_only_fields = ('date_created', 'date_modified')

        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     return data['quest']


class RoundActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundActivity
        fields = ('id', 'activity')
        read_only_fields = ('date_created', 'date_modified')

        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     return data['activity']


class RoundSerializer(serializers.ModelSerializer):
    quests = RoundQuestSerializer(many=True, source='round_quest')
    condition = RoundQuestSerializer(many=True, source='round_condition')
    activities = RoundActivitySerializer(many=True, source='round_activity')

    class Meta:
        model = Round
        fields = (
            'id', 'game', 'name', 'description', 'image', 'order', 'replay', 'stage', 'quests', 'activities',
            'condition')
        read_only_fields = ('date_created', 'date_modified')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['quests'] = [item['quest'] for item in data['quests']]
    #     data['activities'] = [item['activity'] for item in data['activities']]
    #     return data

    def to_internal_value(self, data):
        value = super(RoundSerializer, self).to_internal_value(data)
        value['quests'] = json.loads(data['quests'])
        value['activities'] = json.loads(data['activities'])
        value['condition'] = json.loads(data['condition'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        quests = validated_data.pop('quests')
        activities = validated_data.pop('activities')
        condition = validated_data.pop('condition')

        instance = Round.objects.create(name=validated_data['name'],
                                        description=validated_data['description'],
                                        image=validated_data['image'],
                                        game=validated_data['game'],
                                        order=validated_data['order'],
                                        replay=validated_data['replay']
                                        )

        for item in quests:
            quest = Quest.objects.get(pk=item)
            RoundQuest.objects.create(quest=quest, round=instance)

        for item in condition:
            quest = Quest.objects.get(pk=item)
            RoundCondition.objects.create(quest=quest, round=instance)

        for item in activities:
            activity = Activity.objects.get(pk=item)
            RoundActivity.objects.create(activity=activity, round=instance)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_quests = RoundQuest.objects.filter(round=instance)
        quests = validated_data.pop('quests')
        existing_activities = RoundActivity.objects.filter(round=instance)
        activities = validated_data.pop('activities')
        existing_conditions = RoundCondition.objects.filter(round=instance)
        conditions = validated_data.pop('condition')

        try:
            existing_quests.exclude(quest__in=quests).delete()
            existing_conditions.exclude(quest__in=conditions).delete()
            existing_activities.exclude(activity__in=activities).delete()
        except (RoundQuest.DoesNotExist, RoundCondition.DoesNotExist, RoundActivity.DoesNotExist) as e:
            pass

        for item in quests:
            quest = Quest.objects.get(pk=item)
            try:
                RoundQuest.objects.get(quest=quest, round=instance)
            except RoundQuest.DoesNotExist:
                RoundQuest.objects.create(quest=quest, round=instance)

        for item in conditions:
            quest = Quest.objects.get(pk=item)
            try:
                RoundCondition.objects.get(quest=quest, round=instance)
            except RoundCondition.DoesNotExist:
                RoundCondition.objects.create(quest=quest, round=instance)

        for item in activities:
            activity = Activity.objects.get(pk=item)
            try:
                RoundActivity.objects.get(activity=activity, round=instance)
            except RoundActivity.DoesNotExist:
                RoundActivity.objects.create(activity=activity, round=instance)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance