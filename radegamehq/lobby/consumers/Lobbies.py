from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from ..action_handler import handle_action
from ..action_types import LobbyActionTypes


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

    def fetch_lobbies(self, event):
        lobbies = event['data']
        self.send_json({
            'type': LobbyActionTypes.ADD_LOBBIES.value,
            'payload': {'lobbies': lobbies}
        })

    def create_lobby(self, event):
        lobby = event['data']
        self.send_json({
            'type': LobbyActionTypes.ADD_LOBBY.value,
            'payload': {'lobby': lobby}
        })

    def delete_lobby(self, event):
        self.send_json({
            'type': LobbyActionTypes.REMOVE_LOBBY.value,
            'payload': event['data']
        })

    def player_delete(self, event):
        self.send_json({
            'type': LobbyActionTypes.REMOVE_PLAYER.value,
            'payload': event['data']
        })

    def player_save(self, event):
        player = event['data']
        self.send_json({
            'type': LobbyActionTypes.ADD_PLAYER.value,
            'payload': {'player': player}
        })

    def send_message(self, event):
        self.send_json({
            'type': LobbyActionTypes.ADD_MESSAGE.value,
            'payload': {'message': event['data']}
        })
