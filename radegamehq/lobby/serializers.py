from rest_framework import serializers

from .models import Lobby, MODES, Player


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=None, required=True)
    lobby = serializers.CharField(required=True)
    user = serializers.IntegerField(required=True)
    game = serializers.IntegerField(required=True)

    color = serializers.IntegerField(required=False, allow_null=True)
    team = serializers.IntegerField(required=False, allow_null=True)
    faction = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        player = Player.create(**validated_data)
        return player

    def update(self, instance, validated_data):
        player = Player.load(instance['name'])
        for key, value in validated_data.items():
            setattr(player, key, value)
        player.save()
        return player


class LobbySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    mode = serializers.ChoiceField(required=True, choices=MODES)
    password = serializers.CharField(required=False, allow_blank=True)

    game = serializers.IntegerField()
    setup = serializers.IntegerField()
    owner = serializers.IntegerField()

    def create(self, validated_data):
        lobby = Lobby.create(**validated_data)
        return lobby

    def update(self, instance, validated_data):
        pass
