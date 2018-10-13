from django.db import transaction
from rest_framework import serializers
from typing import Dict

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField

from ..entities.Condition import ConditionClause, Condition


class QuestConditionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ConditionClause
        fields = (
            'id', 'type', 'quest', 'activity', 'resource', 'field', 'keyword', 'amount', 'at_round',
            'by_round')


class QuestSerializer(serializers.ModelSerializer):
    condition = QuestConditionSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Condition
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

        quest = Condition.objects.create(name=validated_data['name'], game=validated_data['game'])

        for item in award:
            self.save_award(item, quest)

        for item in penalty:
            self.save_penalty(item, quest)

        for item in condition:
            self.save_condition(item, quest)

        quest.__dict__.update(**validated_data)
        quest.stage = validated_data['stage']
        quest.save()
        return quest

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_condition = ConditionClause.objects.filter(owner=instance)
        condition = validated_data.pop('condition')
        condition_ids = [item['id'] for item in condition if 'id' in item]

        try:
            existing_condition.exclude(pk__in=condition_ids).delete()
        except ConditionClause.DoesNotExist:
            pass

        for item in condition:
            try:
                obj = ConditionClause.objects.get(pk=item['id'])
                self.save_condition(item, instance, obj)
            except (KeyError, ConditionClause.DoesNotExist) as e:
                self.save_condition(item, instance)

        instance.__dict__.update(**validated_data)
        instance.stage = validated_data['stage']
        instance.save()
        return instance

    @classmethod
    def save_condition(cls, item: Dict[str, any], owner: Condition, obj=None) -> ConditionClause:
        if obj is None:
            obj = ConditionClause(owner=owner, type=item['type'], )

        obj.__dict__.update(**item)
        obj.resource = item['resource']
        obj.quest = item['quest']
        obj.field = item['field']
        obj.at_round = item['at_round']
        obj.by_round = item['by_round']
        obj.activity = item['activity']
        obj.save()
        return obj
