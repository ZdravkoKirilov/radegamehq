from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from arena.models import GameInstance
from shared.signals import handle_lobby_socket_action
from ..action_types import LobbyActionTypes
from ..models import Player


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
        handle_lobby_socket_action.send(LobbyConsumer, data={"action": action, "lobby": self.lobby_name})

    def player_save(self, event):
        player: Player = event['data']
        self.send_json({
            'type': LobbyActionTypes.ADD_PLAYER.value,
            'payload': {'player': player}
        })

    def start_game(self, event):
        game_instance: GameInstance = event['data']['game']
        self.send_json({
            'type': LobbyActionTypes.START_GAME.value,
            'payload': {'game': game_instance}
        })

    def send_message(self, event):
        self.send_json({
            'type': LobbyActionTypes.ADD_MESSAGE.value,
            'payload': {'message': event['data']}
        })
