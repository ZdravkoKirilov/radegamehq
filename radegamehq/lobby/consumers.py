from channels.generic.websocket import JsonWebsocketConsumer
from .signals import lobby_created, lobby_deleted, player_deleted, player_saved, handle_action, send_message
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class LobbyConsumer(JsonWebsocketConsumer):
    channel_layer_alias = 'lobbies'

    lobby_name: str
    lobby_group_name: str

    def connect(self):
        self.lobby_name = self.scope['url_route']['kwargs']['lobby_name']
        self.lobby_group_name = 'lobby_%s' % self.lobby_name

        async_to_sync(self.channel_layer.group_add)(
            self.lobby_group_name,
            self.channel_name
        )

        self.accept()
        self.send_json({'message': '%s connected!' % self.lobby_group_name})

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.lobby_group_name,
            self.channel_name
        )

    def receive_json(self, action, **kwargs):

        if action['type'] == '[Lobby] SEND_MESSAGE':
            payload = action['payload']

            async_to_sync(self.channel_layer.group_send)(
                self.lobby_group_name,
                {
                    "type": "send.message",
                    "data": payload,
                },
            )

    def send_message(self, event):
        self.send_json({
            'type': '[Lobby] SAVE_MESSAGE',
            'payload': event['data']
        })


class LobbiesConsumer(JsonWebsocketConsumer):
    channel_layer_alias = 'lobbies'
    group_name = 'lobbies_list'

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send_json({'message': 'Lobbies socket connected!'})

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive_json(self, content, **kwargs):
        action = content
        handle_action.send(LobbiesConsumer, data=action)

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

    def send_message(self, event):
        self.send_json({
            'type': '[Lobby] SAVE_MESSAGE',
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
