from django.db import transaction
from rest_framework import serializers
from typing import Dict

from ..entities.Faction import Faction, FactionResource, FactionIncome
from ..entities.Activity import ActivityQuota
from .Activity import ActivityQuotaSerializer
from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField


class FactionResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactionResource
        fields = ('id', 'faction', 'resource', 'amount')
        read_only_fields = ('date_created', 'date_modified')


class FactionSerializer(serializers.ModelSerializer):
    resources = FactionResourceSerializer(many=True, source='faction_resource')
    income = FactionResourceSerializer(many=True, source='faction_income')
    activities = ActivityQuotaSerializer(many=True, source='faction_quota')
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Faction
        fields = (
            'id', 'name', 'description', 'keywords', 'image', 'game', 'start', 'type', 'activity_limit',
            'resource_limit', 'resources', 'income', 'activities')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(FactionSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        resources = validated_data.pop('faction_resource')
        income = validated_data.pop('faction_income')
        activities = validated_data.pop('faction_quota')

        faction = Faction.objects.create(name=validated_data['name'], game=validated_data['game'])
        faction.__dict__.update(**validated_data)
        faction.save()

        for item in resources:
            self.save_resource(item, faction)

        for item in income:
            self.save_income(item, faction)

        for item in activities:
            self.save_quota(item, faction)

        return faction

    @transaction.atomic
    def update(self, instance, validated_data):
        existing_resources = FactionResource.objects.filter(faction=instance)
        resources = validated_data.pop('faction_resource')
        resource_ids = [item['id'] for item in resources if 'id' in item]

        existing_income = FactionIncome.objects.filter(faction=instance)
        income = validated_data.pop('faction_income')
        income_ids = [item['id'] for item in income if 'id' in item]

        existing_quota = ActivityQuota.objects.filter(faction=instance)
        activities = validated_data.pop('faction_quota')
        quota_ids = [item['id'] for item in activities if 'id' in item]

        instance.__dict__.update(**validated_data)
        instance.start = validated_data['start']
        instance.save()

        try:
            existing_resources.exclude(pk__in=resource_ids).delete()
            existing_income.exclude(pk__in=income_ids).delete()
            existing_quota.exclude(pk__in=quota_ids).delete()
        except (FactionResource.DoesNotExist, FactionIncome.DoesNotExist, ActivityQuota.DoesNotExist) as e:
            pass

        for item in resources:
            try:
                obj = FactionResource.objects.get(pk=item['id'])
                self.save_resource(item, instance, obj)
            except (KeyError, FactionResource.DoesNotExist) as e:
                self.save_resource(item, instance)

        for item in income:
            try:
                obj = FactionIncome.objects.get(pk=item['id'])
                self.save_income(item, instance, obj)
            except (KeyError, FactionIncome.DoesNotExist) as e:
                self.save_income(item, instance)

        for item in activities:
            try:
                obj = ActivityQuota.objects.get(pk=item['id'])
                self.save_quota(item, instance, obj)
            except (KeyError, ActivityQuota.DoesNotExist) as e:
                self.save_quota(item, instance)

        return instance

    @classmethod
    def save_income(cls, item: Dict[str, any], faction: Faction, obj=None) -> FactionIncome:
        if obj is None:
            obj = FactionIncome(faction=faction, resource=item['resource'], amount=item['amount'])

        obj.__dict__.update(**item)
        obj.save()
        return obj

    @classmethod
    def save_resource(cls, item: Dict[str, any], faction: Faction, obj=None) -> FactionResource:
        if obj is None:
            obj = FactionResource(faction=faction, resource=item['resource'], amount=item['amount'])

        obj.__dict__.update(**item)
        obj.save()
        return obj

    @classmethod
    def save_quota(cls, item: Dict[str, any], faction: Faction, obj=None) -> ActivityQuota:
        if obj is None:
            obj = ActivityQuota(activity=item['activity'], faction=faction)

        obj.__dict__.update(**item)
        obj.save()
        return obj
