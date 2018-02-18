from rest_framework import serializers
from .models import Game, BoardField, MapLocation, Map, MapPath, Resource, FieldIncome, FieldCost, Faction, \
    FactionResource, FactionIncome, Round, RoundQuest, RoundActivity, RoundCondition, FieldQuest, FieldActivity, \
    Activity, ActivityConfig, Quest, QuestCost, QuestCondition, QuestAward, QuestPenalty, Trivia, TriviaAnswer, \
    TriviaAnswerEffect, Stage
from django.db import transaction
import json
import copy


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'boardType', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


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
        fields = ('id', 'game', 'name', 'description', 'image', 'order', 'replay', 'quests', 'activities', 'condition')
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
        fields = ('id', 'name', 'description', 'image', 'game', 'cost', 'condition', 'award', 'penalty')
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


class ActivityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityConfig
        fields = ('id', 'type', 'mode', 'target', 'amount', 'resource')
        read_only_fields = ('date_created', 'date_modified')


class ActivitySerializer(serializers.ModelSerializer):
    configs = ActivityConfigSerializer(many=True, source='config')

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'image', 'game', 'configs')
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
                                           game=validated_data['game'])

        for item in configs:
            obj = ActivityConfig(activity=activity,
                                 mode=item['mode'],
                                 target=item['target'],
                                 type=item['type'], )

            if 'resource' in item:
                resource = Resource.objects.get(pk=item['resource'])
                obj.resource = resource
            if 'amount' in item:
                obj.amount = item['amount']

            obj.save()

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
                                                    mode=item['mode'],
                                                    target=item['target'],
                                                    type=item['type'], )

            if 'resource' in item:
                resource = Resource.objects.get(pk=item['resource'])
                obj.resource = resource

            if 'amount' in item:
                obj.amount = item['amount']

            obj.save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


class FieldQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldQuest
        fields = ('id', 'quest',)
        read_only_fields = ('date_created', 'date_modified')


class FieldActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldActivity
        fields = ('id', 'activity',)
        read_only_fields = ('date_created', 'date_modified')


class FieldResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldIncome
        fields = ('id', 'field', 'resource', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


class BoardFieldSerializer(serializers.ModelSerializer):
    income = FieldResourceSerializer(many=True, source='field_income')
    cost = FieldResourceSerializer(many=True, source='field_cost')
    quests = FieldQuestSerializer(many=True, source='field_quest')
    activities = FieldActivitySerializer(many=True, source='field_activity')

    class Meta:
        model = BoardField
        fields = ('id', 'name', 'description', 'image', 'game', 'income', 'cost', 'quests', 'activities')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(BoardFieldSerializer, self).to_internal_value(data)
        value['income'] = json.loads(data['income'])
        value['cost'] = json.loads(data['cost'])
        value['quests'] = json.loads(data['quests'])
        value['activities'] = json.loads(data['activities'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        income = validated_data.pop('income')
        cost = validated_data.pop('cost')
        quests = validated_data.pop('quests')
        activities = validated_data.pop('activities')
        field = BoardField.objects.create(name=validated_data['name'], description=validated_data['description'],
                                          image=validated_data['image'], game=validated_data['game'])

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            FieldIncome.objects.create(field=field, resource=resource, quantity=item['quantity'])

        for item in cost:
            resource = Resource.objects.get(pk=item['resource'])
            FieldCost.objects.create(field=field, resource=resource, quantity=item['quantity'])
        for item in quests:
            quest = Quest.objects.get(pk=item)
            FieldQuest.objects.create(quest=quest, field=field)
        for item in activities:
            activity = Activity.objects.get(pk=item)
            FieldActivity.objects.create(activity=activity, field=field)

        return field

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_income = FieldIncome.objects.filter(field=instance)
        income = validated_data.pop('income')
        income_ids = [item['id'] for item in income if 'id' in item]

        existing_cost = FieldCost.objects.filter(field=instance)
        cost = validated_data.pop('cost')
        cost_ids = [item['id'] for item in cost if 'id' in item]

        existing_quests = FieldQuest.objects.filter(field=instance)
        quests = validated_data.pop('quests')

        existing_activities = FieldActivity.objects.filter(field=instance)
        activities = validated_data.pop('activities')

        try:
            existing_income.exclude(pk__in=income_ids).delete()
            existing_cost.exclude(pk__in=cost_ids).delete()
            existing_quests.exclude(quest__in=quests).delete()
            existing_activities.exclude(activity__in=activities).delete()
        except (
                FieldIncome.DoesNotExist, FieldCost.DoesNotExist, FieldQuest.DoesNotExist,
                FieldActivity.DoesNotExist) as e:
            pass

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            try:
                obj = FieldIncome.objects.get(pk=item['id'])
            except KeyError:
                FieldIncome.objects.create(field=instance, resource=resource, quantity=item['quantity'])
            else:
                obj.quantity = item['quantity']
                obj.save()

        for item in cost:
            resource = Resource.objects.get(pk=item['resource'])
            try:
                obj = FieldCost.objects.get(pk=item['id'])
            except KeyError:
                FieldCost.objects.create(field=instance, resource=resource, quantity=item['quantity'])
            else:
                obj.quantity = item['quantity']
                obj.save()

        for item in quests:
            quest = Quest.objects.get(pk=item)
            try:
                FieldQuest.objects.get(quest=quest, field=instance)
            except FieldQuest.DoesNotExist:
                FieldQuest.objects.create(field=instance, quest=quest)

        for item in activities:
            activity = Activity.objects.get(pk=item)
            try:
                FieldActivity.objects.get(activity=activity, field=instance)
            except FieldActivity.DoesNotExist:
                FieldActivity.objects.create(field=instance, activity=activity)

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = ('id', 'width', 'height', 'top', 'left', 'game', 'field')
        read_only_fields = ('date_created', 'date_modified')


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'image', 'game',)
        read_only_fields = ('date_created', 'date_modified')


class MapPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPath
        fields = ('id', 'game', 'fromLoc', 'toLoc')
        read_only_fields = ('date_created', 'date_modified')


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'description', 'image', 'game')
        read_only_fields = ('date_created', 'date_modified')


class FactionResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactionResource
        fields = ('id', 'faction', 'resource', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


# class FactionIncomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FactionIncome
#         fields = ('id', 'faction', 'resource', 'quantity')
#         read_only_fields = ('date_created', 'date_modified')


class FactionSerializer(serializers.ModelSerializer):
    resources = FactionResourceSerializer(many=True, source='faction_resource')
    income = FactionResourceSerializer(many=True, source='faction_income')

    class Meta:
        model = Faction
        fields = ('id', 'name', 'description', 'image', 'game', 'resources', 'income')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(FactionSerializer, self).to_internal_value(data)
        value['resources'] = json.loads(data['resources'])
        value['income'] = json.loads(data['income'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        resources = validated_data.pop('resources')
        income = validated_data.pop('income')
        faction = Faction.objects.create(name=validated_data['name'], description=validated_data['description'],
                                         image=validated_data['image'], game=validated_data['game'])
        for item in resources:
            resource = Resource.objects.get(pk=item['resource'])
            FactionResource.objects.create(faction=faction, resource=resource, quantity=item['quantity'])

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            FactionIncome.objects.create(faction=faction, resource=resource, quantity=item['quantity'])

        return faction

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_resources = FactionResource.objects.filter(faction=instance)
        resources = validated_data.pop('resources')
        resource_ids = [item['id'] for item in resources if 'id' in item]

        existing_income = FactionIncome.objects.filter(faction=instance)
        income = validated_data.pop('income')
        income_ids = [item['id'] for item in income if 'id' in item]

        try:
            existing_resources.exclude(pk__in=resource_ids).delete()
            existing_income.exclude(pk__in=income_ids).delete()
        except (FactionResource.DoesNotExist, FactionIncome.DoesNotExist) as e:
            pass

        for item in resources:
            resource = Resource.objects.get(pk=item['resource'])
            try:
                obj = FactionResource.objects.get(pk=item['id'])
            except KeyError:
                FactionResource.objects.create(faction=instance, resource=resource, quantity=item['quantity'])
            else:
                obj.quantity = item['quantity']
                obj.save()

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            try:
                obj = FactionIncome.objects.get(pk=item['id'])
            except KeyError:
                FactionIncome.objects.create(faction=instance, resource=resource, quantity=item['quantity'])
            else:
                obj.quantity = item['quantity']
                obj.save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance


class TriviaAnswerEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaAnswerEffect
        fields = ('id', 'activity')
        read_only_fields = ('date_created', 'date_modified')


class TriviaAnswerSerializer(serializers.ModelSerializer):
    effect = TriviaAnswerEffectSerializer(many=True, source='trivia_answer_effect')

    class Meta:
        model = TriviaAnswer
        fields = ('id', 'description', 'image', 'effect')
        read_only_fields = ('date_created', 'date_modified')


class TriviaSerializer(serializers.ModelSerializer):
    answers = TriviaAnswerSerializer(many=True, source='trivia_answer')

    class Meta:
        model = Trivia
        fields = ('id', 'name', 'description', 'image', 'game', 'mode', 'answers')
        read_only_fields = ('date_created', 'date_modified')

    def serialize_nested(self, data, nested_prop):
        result = dict()
        new_data = copy.deepcopy(data)

        for key, value in data.items():
            if nested_prop in key:
                index = key[len(nested_prop) + 1]
                prop = key[len(nested_prop) + 4:len(key) - 1]
                if index not in result:
                    result[index] = dict()
                result[index][prop] = value

                del new_data[key]

        new_data[nested_prop] = [result[key] for key in result]
        return new_data

    def to_internal_value(self, data):
        data = self.serialize_nested(data, 'answers')
        value = super(TriviaSerializer, self).to_internal_value(data)
        value['answers'] = data['answers']
        return value

    @transaction.atomic
    def create(self, validated_data):
        answers = validated_data.pop('answers')
        instance = Trivia.objects.create(name=validated_data['name'],
                                         description=validated_data['description'],
                                         mode=validated_data['mode'],
                                         game=validated_data['game'],
                                         image=validated_data['image'])
        for item in answers:
            TriviaAnswer.objects.create(trivia=instance, description=item['description'], image=item['image'])

        return instance


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'name', 'description', 'image', 'game')
        read_only_fields = ('date_created', 'date_modified')

    @transaction.atomic
    def update(self, instance, validated_data):

        if 'name' in validated_data:
            instance.name = validated_data.pop('name')
        if 'description' in validated_data:
            instance.description = validated_data.pop('description')
        if 'image' in validated_data:
            instance.image = validated_data.pop('image')

        instance.save()
        return instance
