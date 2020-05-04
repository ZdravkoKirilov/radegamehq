import django.dispatch

lobby_created = django.dispatch.Signal(providing_args=['data'])
lobby_deleted = django.dispatch.Signal(providing_args=['data'])
lobbies_fetched = django.dispatch.Signal(providing_args=['data'])
player_saved = django.dispatch.Signal(providing_args=['data'])
player_deleted = django.dispatch.Signal(providing_args=['data'])
send_message = django.dispatch.Signal(providing_args=['data'])
game_created = django.dispatch.Signal(providing_args=['data'])

handle_lobby_socket_action = django.dispatch.Signal(providing_args=['data'])