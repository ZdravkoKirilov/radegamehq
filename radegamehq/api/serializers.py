from rest_framework import serializers
from .models import Game, BoardField, MapLocation, Map, MapPath, Resource, FieldIncome
from django.db import transaction
import json


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'boardType', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class FieldIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldIncome
        fields = ('id', 'field', 'resource', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


class BoardFieldSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(
    #     max_length=None, use_url=True
    #
    income = FieldIncomeSerializer(many=True, source='field_income')

    class Meta:
        model = BoardField
        fields = ('id', 'name', 'description', 'image', 'game', 'income')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        value = super(BoardFieldSerializer, self).to_internal_value(data)
        value['income'] = json.loads(data['income'])
        return value

    @transaction.atomic
    def create(self, validated_data):
        income = validated_data.pop('income')
        field = BoardField.objects.create(name=validated_data['name'], description=validated_data['description'],
                                          image=validated_data['image'], game=validated_data['game'])

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            FieldIncome.objects.create(field=field, resource=resource, quantity=item['quantity'])

        return field

    @transaction.atomic
    def update(self, instance, validated_data):
        # existing_income = FieldIncome.objects.filter(field=instance)
        income = validated_data.pop('income')

        for item in income:
            resource = Resource.objects.get(pk=item['resource'])
            try:
                obj = FieldIncome.objects.get(pk=item['id'])
            except KeyError:
                FieldIncome.objects.create(field=instance, resource=resource, quantity=item['quantity'])
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


class FieldIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = ('id', 'field', 'income', 'quantity')
        read_only_fields = ('date_created', 'date_modified')


class MapSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(
    #     max_length=None, use_url=True
    # )
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
