import django.dispatch
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver

lobby_created = django.dispatch.Signal(providing_args=['data'])

lobby_deleted = django.dispatch.Signal(providing_args=['data'])

lobbies_fetched = django.dispatch.Signal(providing_args=['data'])

player_saved = django.dispatch.Signal(providing_args=['data'])

player_deleted = django.dispatch.Signal(providing_args=['data'])

send_message = django.dispatch.Signal(providing_args=['data'])

game_created = django.dispatch.Signal(providing_args=['data'])

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
    async_to_sync(layer.group_send)(
        lobby,
        {
            "type": "game.starting",
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
