import django.dispatch
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver

from .models import Player
from .serializers import PlayerSerializer

lobby_created = django.dispatch.Signal(providing_args=['data'])

lobby_deleted = django.dispatch.Signal(providing_args=['data'])

player_saved = django.dispatch.Signal(providing_args=['data'])

player_deleted = django.dispatch.Signal(providing_args=['data'])

player_updated = django.dispatch.Signal(providing_args=['data'])

send_message = django.dispatch.Signal(providing_args=['data'])

handle_action = django.dispatch.Signal(providing_args=['data'])

game_created = django.dispatch.Signal(providing_args=['data'])


@receiver(game_created)
def handle_game_created(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    lobby = 'lobby_%s' % kwargs['data']['lobby']
    async_to_sync(layer.group_send)(
        lobby,
        {
            "type": "game.starting",
            "data": kwargs['data'],
        },
    )


@receiver(lobby_created)
def handle_lobby_created(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        "lobbies_list",
        {
            "type": "lobby.create",
            "data": kwargs['data'],
        },
    )


@receiver(lobby_deleted)
def handle_lobby_deleted(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        "lobbies_list",
        {
            "type": "lobby.delete",
            "data": kwargs['data'],
        },
    )


@receiver(player_deleted)
def handle_player_deleted(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        "lobbies_list",
        {
            "type": "player.delete",
            "data": kwargs['data'],
        },
    )


@receiver(player_saved)
def handle_player_saved(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        "lobbies_list",
        {
            "type": "player.save",
            "data": kwargs['data'],
        },
    )


@receiver(player_updated)
def handle_player_updated(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    lobby = 'lobby_%s' % kwargs['data']['lobby']
    async_to_sync(layer.group_send)(
        lobby,
        {
            "type": "player.update",
            "data": kwargs['data'],
        },
    )


@receiver(send_message)
def handle_message_sent(sender, **kwargs):
    layer = get_channel_layer(alias='lobbies')
    async_to_sync(layer.group_send)(
        "lobbies_list",
        {
            "type": "send.message",
            "data": kwargs['data'],
        },
    )


@receiver(handle_action)
def handle_generic_action(sender, **kwargs):
    action = kwargs['data']

    if action['type'] == '[Lobby] DELETE_PLAYER':
        payload = action['payload']

        try:
            player = Player.load(payload)
            player.delete()
            player_deleted.send('action_handler', data=payload)
        except KeyError:
            pass

    if action['type'] == '[Lobby] UPDATE_PLAYER':
        payload = action['payload']
        try:
            player = Player.load(payload['name'])
            validated_data = PlayerSerializer(payload).data
            for key, value in validated_data.items():
                setattr(player, key, value)
            player.save()
            player_updated.send('action_handler', data=PlayerSerializer(player).data)
        except KeyError:
            pass

    if action['type'] == '[Lobby] CREATE_PLAYER':
        payload = action['payload']
        player = PlayerSerializer(payload)

        player.create(player.data)
        player_saved.send('action_handler', data=player.data)

    if action['type'] == '[Lobby] SEND_MESSAGE':
        payload = action['payload']

        send_message.send('action_handler', data=payload)
