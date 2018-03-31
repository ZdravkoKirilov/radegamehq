import copy

from django.db import transaction
from rest_framework import serializers

from api.entities.Game import Game
from api.entities.Stage import Stage


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'name', 'description', 'image', 'game')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, input_data):
        data = copy.deepcopy(input_data)
        if 'image' in data and data['image'] == 'null':
            data['image'] = None
        data['game'] = Game.objects.get(pk=data['game'])
        return data

    @transaction.atomic
    def update(self, instance, validated_data):

        if 'name' in validated_data:
            instance.name = validated_data.pop('name')
        if 'description' in validated_data:
            instance.description = validated_data.pop('description')
        if 'image' in validated_data and type(validated_data['image']) is not str:
            if validated_data['image'] is not None:
                instance.image = validated_data.pop('image')
            else:
                instance.image = None

        instance.save()
        return instance