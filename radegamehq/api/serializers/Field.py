import json

from django.db import transaction
from rest_framework import serializers

from api.entities.Activity import Activity
from api.entities.Field import FieldQuest, FieldActivity, FieldIncome, Field, FieldCost
from api.entities.Quest import Quest
from api.entities.Resource import Resource


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
        model = Field
        fields = (
            'id', 'name', 'description', 'image', 'keywords', 'game', 'stage', 'income', 'cost', 'quests', 'activities')
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

        field = Field.objects.create(name=validated_data['name'], description=validated_data['description'],
                                     image=validated_data['image'], game=validated_data['game'],
                                     stage=validated_data['stage'])

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
