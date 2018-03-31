import json

from django.db import transaction
from rest_framework import serializers

from api.entities.Activity import Activity
from api.entities.Field import BoardField
from api.entities.Quest import QuestCost, QuestCondition, QuestAward, QuestPenalty, Quest
from api.entities.Resource import Resource
from api.entities.Round import Round


class QuestCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestCost
        fields = ('id', 'activity',)
        read_only_fields = ('date_created', 'date_modified')


class QuestConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestCondition
        fields = ('id', 'type', 'owner', 'quest', 'activity', 'resource', 'field', 'amount', 'atRound', 'byRound')
        read_only_fields = ('date_created', 'date_modified')


class QuestAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestAward
        fields = ('id', 'activity',)
        read_only_fields = ('date_created', 'date_modified')


class QuestPenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestPenalty
        fields = ('id', 'activity',)
        read_only_fields = ('date_created', 'date_modified')


class QuestSerializer(serializers.ModelSerializer):
    cost = QuestCostSerializer(many=True, source='quest_cost')
    condition = QuestConditionSerializer(many=True, source='quest_condition')
    award = QuestAwardSerializer(many=True, source='quest_award')
    penalty = QuestPenaltySerializer(many=True, source='quest_penalty')

    class Meta:
        model = Quest
        fields = ('id', 'name', 'description', 'image', 'game', 'stage', 'cost', 'condition', 'award', 'penalty')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(QuestSerializer, self).to_internal_value(data)
        value['cost'] = json.loads(data['cost'])
        value['condition'] = json.loads(data['condition'])
        value['award'] = json.loads(data['award'])
        value['penalty'] = json.loads(data['penalty'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        cost = validated_data.pop('cost')
        condition = validated_data.pop('condition')
        award = validated_data.pop('award')
        penalty = validated_data.pop('penalty')

        quest = Quest.objects.create(name=validated_data['name'],
                                     description=validated_data['description'],
                                     image=validated_data['image'],
                                     game=validated_data['game'])

        for item in cost:
            activity = Activity.objects.get(pk=item)
            QuestCost.objects.create(quest=quest, activity=activity, )

        for item in award:
            activity = Activity.objects.get(pk=item)
            QuestAward.objects.create(quest=quest, activity=activity, )

        for item in penalty:
            activity = Activity.objects.get(pk=item)
            QuestPenalty.objects.create(quest=quest, activity=activity, )

        for item in condition:
            obj = QuestCondition(owner=quest, type=item['type'], )

            if 'resource' in item and item['resource'] is not None:
                resource = Resource.objects.get(pk=item['resource'])
                obj.resource = resource
            if 'amount' in item and item['amount'] is not None:
                obj.amount = item['amount']
            if 'quest' in item and item['quest'] is not None:
                quest = Quest.objects.get(pk=item['quest'])
                obj.quest = quest
            if 'activity' in item and item['activity'] is not None:
                activity = Activity.objects.get(pk=item['activity'])
                obj.activity = activity
            if 'field' in item and item['field'] is not None:
                field = BoardField.objects.get(pk=item['field'])
                obj.field = field
            if 'byRound' in item and item['byRound'] is not None:
                by_round = Round.objects.get(pk=item['byRound'])
                obj.byRound = by_round
            if 'atRound' in item and item['atRound'] is not None:
                at_round = Round.objects.get(pk=item['atRound'])
                obj.atRound = at_round

            obj.save()

        return quest

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_condition = QuestCondition.objects.filter(owner=instance)
        condition = validated_data.pop('condition')
        condition_ids = [item['id'] for item in condition if 'id' in item]

        existing_cost = QuestCost.objects.filter(quest=instance)
        existing_cost_ids = [item.activity.id for item in existing_cost]
        cost = validated_data.pop('cost')

        existing_award = QuestAward.objects.filter(quest=instance)
        existing_award_ids = [item.activity.id for item in existing_award]
        award = validated_data.pop('award')

        existing_penalty = QuestPenalty.objects.filter(quest=instance)
        existing_penalty_ids = [item.activity.id for item in existing_penalty]
        penalty = validated_data.pop('penalty')

        try:
            existing_condition.exclude(pk__in=condition_ids).delete()
            existing_cost.exclude(activity__in=cost).delete()
            existing_award.exclude(activity__in=award).delete()
            existing_penalty.exclude(activity__in=penalty).delete()
        except (
                QuestCost.DoesNotExist, QuestCondition.DoesNotExist, QuestAward.DoesNotExist,
                QuestPenalty.DoesNotExist) as e:
            pass

        for item in cost:
            if item not in existing_cost_ids:
                activity = Activity.objects.get(pk=item)
                QuestCost.objects.create(quest=instance, activity=activity)

        for item in award:
            if item not in existing_award_ids:
                activity = Activity.objects.get(pk=item)
                QuestAward.objects.create(quest=instance, activity=activity)

        for item in penalty:
            if item not in existing_penalty_ids:
                activity = Activity.objects.get(pk=item)
                QuestPenalty.objects.create(quest=instance, activity=activity)

        for item in condition:
            try:
                obj = QuestCondition.objects.get(pk=item['id'])
            except KeyError:
                obj = QuestCondition.objects.create(owner=instance, type=item['type'], )

            if 'resource' in item:
                resource = Resource.objects.get(pk=item['resource'])
                obj.resource = resource
            if 'amount' in item:
                obj.amount = item['amount']
            if 'quest' in item:
                quest = Quest.objects.get(pk=item['quest'])
                obj.quest = quest
            if 'activity' in item:
                activity = Activity.objects.get(pk=item['activity'])
                obj.activity = activity
            if 'field' in item:
                field = BoardField.objects.get(pk=item['field'])
                obj.field = field
            if 'byRound' in item and item['byRound'] is not None:
                by_round = Round.objects.get(pk=item['byRound'])
                obj.byRound = by_round
            if 'atRound' in item and item['atRound'] is not None:
                at_round = Round.objects.get(pk=item['atRound'])
                obj.atRound = at_round

            obj.save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance