from django.db import transaction
from rest_framework import serializers
from typing import Dict

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField

from ..entities.Activity import Activity
from ..entities.Field import Field
from ..entities.Quest import QuestCondition, QuestAward, QuestPenalty, Quest
from ..entities.Resource import Resource
from ..entities.Round import Round


class QuestConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestCondition
        fields = (
            'id', 'type', 'owner', 'quest', 'activity', 'resource', 'field', 'keyword', 'amount', 'at_round',
            'by_round')


class QuestAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestAward
        fields = ('id', 'activity',)


class QuestPenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestPenalty
        fields = ('id', 'activity',)


class QuestSerializer(serializers.ModelSerializer):
    condition = QuestConditionSerializer(many=True, source='quest_condition')
    award = QuestAwardSerializer(many=True, source='quest_award')
    penalty = QuestPenaltySerializer(many=True, source='quest_penalty')
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Quest
        fields = (
            'id', 'name', 'description', 'keywords', 'image', 'game', 'stage', 'condition', 'award', 'penalty')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(QuestSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        condition = validated_data.pop('condition')
        award = validated_data.pop('award')
        penalty = validated_data.pop('penalty')

        quest = Quest.objects.create(name=validated_data['name'], game=validated_data['game'])

        for item in award:
            self.save_award(item, quest)

        for item in penalty:
            self.save_penalty(item, quest)

        for item in condition:
            self.save_condition(item, quest)

        quest.__dict__.update(**validated_data)
        quest.save()
        return quest

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_condition = QuestCondition.objects.filter(owner=instance)
        condition = validated_data.pop('condition')
        condition_ids = [item['id'] for item in condition if 'id' in item]

        existing_award = QuestAward.objects.filter(quest=instance)
        existing_award_ids = [item.activity.id for item in existing_award]
        award = validated_data.pop('award')

        existing_penalty = QuestPenalty.objects.filter(quest=instance)
        existing_penalty_ids = [item.activity.id for item in existing_penalty]
        penalty = validated_data.pop('penalty')

        try:
            existing_condition.exclude(pk__in=condition_ids).delete()
            existing_award.exclude(activity__in=award).delete()
            existing_penalty.exclude(activity__in=penalty).delete()
        except (
                QuestCondition.DoesNotExist, QuestAward.DoesNotExist,
                QuestPenalty.DoesNotExist) as e:
            pass

        for item in award:
            if item not in existing_award_ids:
                self.save_award(item, instance)

        for item in penalty:
            if item not in existing_penalty_ids:
                self.save_penalty(item, instance)

        for item in condition:
            try:
                obj = QuestCondition.objects.get(pk=item['id'])
                self.save_condition(item, instance, obj)
            except (KeyError, QuestCondition.DoesNotExist) as e:
                self.save_condition(item, instance)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_condition(cls, item: Dict[str, any], owner: Quest, obj=None) -> QuestCondition:
        if obj is None:
            obj = QuestCondition(owner=owner, type=item['type'], )

        obj.__dict__.update(**item)
        obj.save()
        return obj

    @classmethod
    def save_award(cls, item: Dict[str, any], owner: Quest, obj=None) -> QuestAward:
        if obj is None:
            obj = QuestAward(quest=owner, activity=item['activity'])

        obj.__dict__.update(**item)
        obj.save()
        return obj

    @classmethod
    def save_penalty(cls, item: Dict[str, any], owner: Quest, obj=None) -> QuestPenalty:
        if obj is None:
            obj = QuestPenalty(quest=owner, activity=item['activity'])

        obj.__dict__.update(**item)
        obj.save()
        return obj
