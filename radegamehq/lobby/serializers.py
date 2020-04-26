import time
from typing import Dict

from rest_framework import serializers
from walrus import Model
import uuid

from .models import Lobby, MODES, Player


class ChatMessageSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=True, allow_blank=True)
    owner = serializers.IntegerField(required=True)  ## user
    lobby = serializers.CharField(allow_null=True, allow_blank=True)  ## Lobby

    timestamp = serializers.IntegerField(allow_null=True)
    message = serializers.CharField(required=True)

    def to_internal_value(self, data: Dict) -> Dict:
        if 'id' not in data or data['id'] is None:
            data['id'] = str(uuid.uuid4())

        if 'timestamp' not in data or data['timestamp'] is None:
            data['timestamp'] = time.time()

        return data


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    lobby = serializers.CharField(required=True)
    user = serializers.IntegerField(required=True)
    game = serializers.IntegerField(required=True)

    data = serializers.DictField(allow_null=True, required=False)

    def create(self, _):
        try:
            self.is_valid()
            validated_data = self.validated_data
            Player.create(**validated_data)
            return self.validated_data
        except Exception as e:
            pass

    def update(self, player: Model, _):
        try:
            self.is_valid()
            player.data.update(self.validated_data['data'])
            player.save()
            return self.validated_data
        except Exception as e:
            pass

    def delete(self, player: Dict):
        try:
            player_entity = Player.load(player['name'])
            data = PlayerSerializer(player).data
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

    def to_internal_value(self, data: Dict) -> Dict:
        data['name'] = str(uuid.uuid4())
        data['timestamp'] = time.time()
        if 'mode' not in data or not data['mode']:
            data['mode'] = MODES[0][0]

        return data

    def create(self):
        self.is_valid()
        Lobby.create(**self.validated_data)
        return self.validated_data

    def update(self, instance, validated_data):
        pass

    def delete(self, lobby: Dict):
        lobby_entity = Lobby.load(lobby['name'])
        lobby_entity.delete()
