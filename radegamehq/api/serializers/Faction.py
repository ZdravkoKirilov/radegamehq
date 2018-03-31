import json

from django.db import transaction
from rest_framework import serializers

from api.entities.Faction import Faction, FactionResource, FactionIncome
from api.entities.Resource import Resource


class FactionResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactionResource
        fields = ('id', 'faction', 'resource', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


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
