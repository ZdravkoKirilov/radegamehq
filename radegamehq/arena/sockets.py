from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class ArenaConsumer(JsonWebsocketConsumer):
    channel_layer_alias = 'lobbies'

    game_name: str
    game_group_name: str

    def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = 'game_%s' % self.game_name

        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
        )

        self.accept()
        # self.send_json({'message': '%s connected!' % self.game_group_name})

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name
        )

    def receive_json(self, actions, **kwargs):

        async_to_sync(self.channel_layer.group_send)(
            self.game_group_name,
            {
                "type": "send.actions",
                "data": actions,
            },
        )

    def send_actions(self, event):
        self.send_json(event['data'])
