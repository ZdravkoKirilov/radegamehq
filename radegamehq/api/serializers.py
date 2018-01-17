from rest_framework import serializers
from .models import Game, BoardField, MapLocation, Map, MapPath, Resource, FieldIncome, FieldCost, Faction, \
    FactionResource, FactionIncome, Action, ActionConfig
from django.db import transaction
import json


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'boardType', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ActionConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionConfig
        fields = ('id', 'type', 'mode', 'target', 'amount', 'resource')
        read_only_fields = ('date_created', 'date_modified')


class ActionSerializer(serializers.ModelSerializer):
    configs = ActionConfigSerializer(many=True, source='config')

    class Meta:
        model = Action
        fields = ('id', 'name', 'description', 'image', 'game', 'configs')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(ActionSerializer, self).to_internal_value(data)
        value['configs'] = json.loads(data['configs'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        configs = validated_data.pop('configs')

        action = Action.objects.create(name=validated_data['name'],
                                       description=validated_data['description'],
                                       image=validated_data['image'],
                                       game=validated_data['game'])

        for item in configs:
            obj = ActionConfig(action=action,
                               mode=item['mode'],
                               target=item['target'],
                               type=item['type'], )

            if 'resource' in item:
                resource = Resource.objects.get(pk=item['resource'])
                obj.resource = resource
            if 'amount' in item:
                obj.amount = item['amount']

            obj.save()

        return action

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_configs = ActionConfig.objects.filter(action=instance)
        configs = validated_data.pop('configs')
        config_ids = [item['id'] for item in configs if 'id' in item]

        try:
            existing_configs.exclude(pk__in=config_ids).delete()
        except ActionConfig.DoesNotExist:
            pass

        for item in configs:
            try:
                obj = ActionConfig.objects.get(pk=item['id'])
            except KeyError:
                obj = ActionConfig.objects.create(action=instance,
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


class FieldResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldIncome
        fields = ('id', 'field', 'resource', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


class BoardFieldSerializer(serializers.ModelSerializer):
    income = FieldResourceSerializer(many=True, source='field_income')
    cost = FieldResourceSerializer(many=True, source='field_cost')

    class Meta:
        model = BoardField
        fields = ('id', 'name', 'description', 'image', 'game', 'income', 'cost')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(BoardFieldSerializer, self).to_internal_value(data)
        value['income'] = json.loads(data['income'])
        value['cost'] = json.loads(data['cost'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        income = validated_data.pop('income')
        cost = validated_data.pop('cost')
        field = BoardField.objects.create(name=validated_data['name'], description=validated_data['description'],
                                          image=validated_data['image'], game=validated_data['game'])

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            FieldIncome.objects.create(field=field, resource=resource, quantity=item['quantity'])

        for item in cost:
            resource = Resource.objects.get(pk=item['resource'])
            FieldCost.objects.create(field=field, resource=resource, quantity=item['quantity'])

        return field

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_income = FieldIncome.objects.filter(field=instance)
        income = validated_data.pop('income')
        income_ids = [item['id'] for item in income if 'id' in item]

        existing_cost = FieldCost.objects.filter(field=instance)
        cost = validated_data.pop('cost')
        cost_ids = [item['id'] for item in cost if 'id' in item]

        try:
            existing_income.exclude(pk__in=income_ids).delete()
            existing_cost.exclude(pk__in=cost_ids).delete()
        except (FieldIncome.DoesNotExist, FieldCost.DoesNotExist) as e:
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
