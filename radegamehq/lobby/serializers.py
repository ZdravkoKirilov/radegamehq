import time
from typing import Dict

from rest_framework import serializers
from walrus import Model
import uuid

from .models import Lobby, MODES, Player
from .types import MessageType, PlayerType, LobbyType


class ChatMessageSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=True, allow_blank=True)
    owner = serializers.IntegerField(required=True)  ## user
    lobby = serializers.CharField(allow_null=True, allow_blank=True)  ## Lobby

    timestamp = serializers.IntegerField(allow_null=True)
    message = serializers.CharField(required=True)

    def to_internal_value(self, data: MessageType) -> Dict:
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = time.time()

        return data


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True, allow_null=True)
    lobby = serializers.CharField(required=True)
    user = serializers.IntegerField(required=True)

    data = serializers.DictField(allow_null=True, required=False)

    def to_internal_value(self, data: PlayerType) -> Dict:
        if 'name' not in data or not data['name']:
            data['name'] = str(uuid.uuid4())
        return data

    def create(self, _):
        try:
            self.is_valid()
            validated_data: PlayerType | Dict = self.validated_data
            Player.create(**validated_data)
            return self.validated_data
        except Exception as e:
            pass

    def update(self, player: Model, _):
        try:
            self.is_valid()
            new_data: PlayerType = self.validated_data['data']
            player.data.update(new_data)
            player.save()
            return self.validated_data
        except Exception as e:
            pass

    def delete(self, player: PlayerType):
        try:
            player_entity = Player.load(player['name'])
            data: PlayerType | Dict = PlayerSerializer(player).data
            player_entity.delete()
            return data
        except Exception as e:
            pass


class LobbySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    timestamp = serializers.IntegerField()
    mode = serializers.ChoiceField(choices=MODES)
    password = serializers.CharField(allow_blank=True)

    game = serializers.IntegerField(required=True)
    setup = serializers.IntegerField(required=True)
    owner = serializers.IntegerField(required=True)

    def to_internal_value(self, data: LobbyType) -> LobbyType:
        data['name'] = str(uuid.uuid4())
        data['timestamp'] = time.time()
        if 'mode' not in data or not data['mode']:
            data['mode'] = MODES[0][0]

        return data

    def create(self, _) -> LobbyType:
        self.is_valid()
        data: LobbyType | Dict = self.validated_data
        Lobby.create(**data)
        return data

    def update(self, instance, validated_data):
        pass

    def delete(self, lobby: LobbyType):
        lobby_entity = Lobby.load(lobby['name'])
        lobby_entity.delete()
