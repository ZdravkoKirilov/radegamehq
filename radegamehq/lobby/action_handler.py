from typing import Dict

from django.dispatch import receiver
import django.dispatch

from .action_types import LobbyActionTypes
from .models import Player, Lobby
from .serializers import PlayerSerializer, LobbySerializer, ChatMessageSerializer
from .signals import player_deleted, player_saved, send_message, lobbies_fetched, lobby_created, \
    lobby_deleted

handle_action = django.dispatch.Signal(providing_args=['data'])


@receiver(handle_action)
def handle_generic_action(sender, **kwargs):
    action = kwargs['data']
    payload: Dict = action['payload']
    action_type: str = action['type']

    if action_type == LobbyActionTypes.FETCH_LOBBIES.value:
        game_id = payload['gameId']
        try:
            lobbies = [lobby for lobby in Lobby.query(Lobby.game == game_id, order_by=Lobby.timestamp)]
            serialized_lobbies = LobbySerializer(lobbies, many=True)
            lobbies_fetched.send('action_handler', data=serialized_lobbies.data)
        except Exception as e:
            pass

    if action_type == LobbyActionTypes.CREATE_LOBBY.value:
        lobby = payload['lobby']
        try:
            serialized_lobby = LobbySerializer(data=lobby)
            serialized_lobby.create()
            lobby_created.send('action_handler', data=serialized_lobby.validated_data)
        except Exception as e:
            pass

    if action_type == LobbyActionTypes.DELETE_LOBBY.value:
        lobby = payload['lobby']

        try:
            serialized_lobby = LobbySerializer(data=lobby)
            serialized_lobby.delete(lobby)
            lobby_deleted.send('action_handler', data=payload)
        except Exception as e:
            pass

    if action_type == LobbyActionTypes.SAVE_PLAYER.value:
        player = payload['player']
        serialized_player = PlayerSerializer(data=player)
        result = None
        try:
            player_entity = Player.load(player['name'])
            result = serialized_player.update(player_entity, None)
        except KeyError:
            result = serialized_player.create(None)
        except Exception as e:
            pass
        finally:
            player_saved.send('action_handler', data=result)

    if action_type == LobbyActionTypes.DELETE_PLAYER.value:

        try:
            player = payload['player']
            player_serializer = PlayerSerializer(data=player)
            result = player_serializer.delete(player)
            player_deleted.send('action_handler', data=result)
        except KeyError:
            pass

    if action_type == LobbyActionTypes.SEND_MESSAGE.value:
        message = payload['message']
        serialized_message = ChatMessageSerializer(data=message)
        serialized_message.is_valid()
        send_message.send('action_handler', data=serialized_message.validated_data)
