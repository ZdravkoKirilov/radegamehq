import django.dispatch

lobby_created = django.dispatch.Signal(providing_args=['data'])

lobby_deleted = django.dispatch.Signal(providing_args=['data'])

player_created = django.dispatch.Signal(providing_args=['data'])

player_deleted = django.dispatch.Signal(providing_args=['data'])
