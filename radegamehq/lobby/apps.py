from django.apps import AppConfig


class LobbyConfig(AppConfig):
    name = 'lobby'

    def ready(self):
        import lobby.receivers
