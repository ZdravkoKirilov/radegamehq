from channels.generic.websocket import JsonWebsocketConsumer
from .signals import lobby_created
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class LobbyConsumer(JsonWebsocketConsumer):
    channel_layer_alias = 'lobbies'

    @staticmethod
    def subscribe_lobby_created():
        lobby_created.connect(handle_lobby_created)

    def connect(self):
        self.accept()
        LobbyConsumer.subscribe_lobby_created()
        async_to_sync(self.channel_layer.group_add)("lobbies_list", self.channel_name)
        self.send_json({'message': 'Connected!'})

    def disconnect(self, code):
        pass

    def receive_json(self, content, **kwargs):
        pass

    def lobby_create(self, event):
        self.send_json({
            'type': 'GOSHO',
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
