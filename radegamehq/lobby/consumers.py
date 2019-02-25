from channels.generic.websocket import JsonWebsocketConsumer

from .models import Player
from .serializers import PlayerSerializer


class LobbyConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self.send_json({'message': 'Connected!'})

    def disconnect(self, code):
        pass

    def receive_json(self, content, **kwargs):
        player = Player.load('tosho')

        room = self.scope['url_route']['kwargs']['lobby_name']

        self.send_json({
            'message': PlayerSerializer(player).data,
            'room': room,
        })
