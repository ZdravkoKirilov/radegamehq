from typing import Dict

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch.dispatcher import receiver

from arena.serializers import GameInstanceSerializer
from lobby.action_types import LobbyActionTypes
from lobby.models import Lobby, Player
from lobby.serializers import LobbySerializer, PlayerSerializer, ChatMessageSerializer
from shared.signals import lobby_created, lobby_deleted, lobbies_fetched, player_saved, player_deleted, send_message, \
    game_created, handle_lobby_socket_action

lobbies_list = 'lobbies_list'
layer_alias = 'lobbies'


@receiver(lobbies_fetched)
def handle_lobbies_fetched(sender, **kwargs):
    layer = get_channel_layer(alias=layer_alias)
    async_to_sync(layer.group_send)(
        lobbies_list,
        {
            "type": "fetch.lobbies",
            "data": kwargs['data'],
        },
    )


@receiver(lobby_created)
def handle_lobby_created(sender, **kwargs):
    layer = get_channel_layer(alias=layer_alias)
    async_to_sync(layer.group_send)(
        lobbies_list,
        {
            "type": "create.lobby",
            "data": kwargs['data'],
        },
    )


@receiver(lobby_deleted)
def handle_lobby_deleted(sender, **kwargs):
    layer = get_channel_layer(alias=layer_alias)
    async_to_sync(layer.group_send)(
        lobbies_list,
        {
            "type": "delete.lobby",
            "data": kwargs['data'],
        },
    )


@receiver(player_saved)
def handle_player_saved(sender, **kwargs):
    layer = get_channel_layer(alias=layer_alias)
    async_to_sync(layer.group_send)(
        lobbies_list,
        {
            "type": "player.save",
            "data": kwargs['data'],
        },
    )


@receiver(game_created)
def handle_game_created(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    lobby = 'lobby_%s' % kwargs['data']['lobby']
    game_instance = kwargs['data']['game']
    async_to_sync(layer.group_send)(
        lobby,
        {
            "type": "start.game",
            "data": {'game': game_instance},
        },
    )


@receiver(player_deleted)
def handle_player_deleted(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        lobbies_list,
        {
            "type": "player.delete",
            "data": kwargs['data'],
        },
    )


@receiver(send_message)
def handle_message_sent(sender, **kwargs):
    try:
        layer = get_channel_layer(alias='lobbies')
        lobby = 'lobby_%s' % kwargs['data']['lobby'] if 'lobby' in kwargs['data'] else None
        target = lobby if lobby else lobbies_list
        data = kwargs['data']

        async_to_sync(layer.group_send)(
            target,
            {
                "type": "send.message",
                "data": data,
            },
        )
    except Exception as e:
        pass


@receiver(handle_lobby_socket_action)
def handle_generic_action(sender, **kwargs):
    action = kwargs['data']['action']
    lobby = kwargs['data']['lobby']
    payload: Dict = action['payload']
    action_type: str = action['type']

    if action_type == LobbyActionTypes.FETCH_LOBBIES.value:
        game_id = payload['gameId']
        try:
            lobbies = [lobby for lobby in Lobby.query(Lobby.game == game_id, order_by=Lobby.timestamp)]
            serialized_lobbies = LobbySerializer(lobbies, many=True)
            lobby_names = [lobby['name'] for lobby in serialized_lobbies.data]
            players = [player for player in Player.all()]
            players_for_game = [player for player in players if player.lobby in lobby_names]
            serialized_player = PlayerSerializer(players_for_game, many=True)
            response = {
                'lobbies': serialized_lobbies.data,
                'players': serialized_player.data,
            }
            lobbies_fetched.send('action_handler', data=response)
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

    if action_type == LobbyActionTypes.CREATE_GAME.value:
        data = payload['game_data']
        try:
            game_data = {
                'game_id': data['game_id'],
                'players': data['players'],
                'setup': data['setup']
            }
            serialized = GameInstanceSerializer(data=game_data)
            serialized.is_valid()
            instance = serialized.save()
            response = {"game": GameInstanceSerializer(instance).data, "lobby": lobby}

            game_created.send('action_handler', data=response)
        except Exception as error:
            pass

    if action_type == LobbyActionTypes.SEND_MESSAGE.value:
        message = payload['message']
        serialized_message = ChatMessageSerializer(data=message)
        serialized_message.is_valid()
        send_message.send('action_handler', data=serialized_message.validated_data)
