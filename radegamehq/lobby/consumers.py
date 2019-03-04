from channels.generic.websocket import JsonWebsocketConsumer
from .signals import lobby_created, lobby_deleted, player_deleted, player_saved, handle_action
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class LobbyConsumer(JsonWebsocketConsumer):
    channel_layer_alias = 'lobbies'
    group_name = 'lobbies_list'

    @staticmethod
    def subscribe_lobby_created():
        lobby_created.connect(handle_lobby_created)

    def connect(self):
        self.accept()
        LobbyConsumer.subscribe_lobby_created()
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send_json({'message': 'Connected!'})

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive_json(self, content, **kwargs):
        action = content
        handle_action.send(LobbyConsumer, data=action)

    def lobby_create(self, event):
        self.send_json({
            'type': '[Lobby] CREATE_LOBBY',
            'payload': event['data']
        })

    def lobby_delete(self, event):
        self.send_json({
            'type': '[Lobby] REMOVE_LOBBY',
            'payload': event['data']
        })

    def player_delete(self, event):
        self.send_json({
            'type': '[Lobby] REMOVE_PLAYER',
            'payload': event['data']
        })

    def player_save(self, event):
        self.send_json({
            'type': '[Lobby] SAVE_PLAYER',
            'payload': event['data']
        })


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
