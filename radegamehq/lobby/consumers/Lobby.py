from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


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

    def player_update(self, event):
        self.send_json({
            'type': '[Lobby] SAVE_PLAYER',
            'payload': event['data']
        })
