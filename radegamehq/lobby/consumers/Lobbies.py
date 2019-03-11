from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from ..signals import handle_action


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