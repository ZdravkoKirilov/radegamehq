from rest_framework import serializers
from .models import Game, BoardField, MapLocation, Map
from .custom_serializers import Base64ImageField


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'boardType', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class BoardFieldSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(
    #     max_length=None, use_url=True
    # )

    class Meta:
        model = BoardField
        fields = ('id', 'name', 'description', 'image', 'game', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = ('id', 'width', 'height', 'top', 'left', 'game', 'field')
        read_only_fields = ('date_created', 'date_modified')


class MapSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(
    #     max_length=None, use_url=True
    # )
    class Meta:
        model = Map
        fields = ('image', 'game',)
        read_only_fields = ('date_created', 'date_modified')
