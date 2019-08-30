from .models import Lobby, Player
from .serializers import LobbySerializer, PlayerSerializer
from arena.serializers import GameInstanceSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
import uuid

from .signals import lobby_created, lobby_deleted, player_deleted, player_saved, player_updated, game_created


class PlayerListView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        try:
            lobby = self.kwargs['pk']
            players = Player.query(Player.lobby == lobby)
        except KeyError:
            players = Player.all()
        items = [player for player in players]
        return items

    def create(self, request, *args, **kwargs):
        player = PlayerSerializer(request.data)
        player_entity = player.create(player.data)
        response = PlayerSerializer(player_entity).data

        player_saved.send(PlayerListView, data=response)

        return Response(response, status=status.HTTP_201_CREATED)


class PlayerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer

    def get_object(self):
        lobby = self.kwargs['pk']
        name = self.kwargs['player']
        query = Player.query((Player.name == name) & (Player.lobby == lobby))
        players = [player for player in query]

        try:
            player = players[0]
            serializer = PlayerSerializer(player)
            return serializer.data
        except IndexError:
            raise Http404()

    def delete(self, request, *args, **kwargs):
        name = self.kwargs['player']
        player = Player.load(name)
        serialized_player = PlayerSerializer(player).data
        player.delete()
        player_deleted.send(PlayerDetailsView, data=serialized_player)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        player_updated.send(PlayerDetailsView, data=response.data)
        return response


class LobbyListView(generics.ListCreateAPIView):
    serializer_class = LobbySerializer

    def get_queryset(self):
        lobbies = Lobby.all()
        items = [item for item in lobbies]
        return items

    def create(self, request, *args, **kwargs):
        lobby = LobbySerializer(request.data['lobby'])
        player = PlayerSerializer(request.data['owner'])

        lobby_entity = lobby.create(lobby.data)
        player_entity = player.create(player.data)

        response = {
            'lobby': LobbySerializer(lobby_entity).data,
            'owner': PlayerSerializer(player_entity).data
        }

        lobby_created.send(LobbyListView, data=response)

        return Response(response, status=status.HTTP_201_CREATED)


class LobbyDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class = LobbySerializer

    def get_object(self):
        try:
            name = self.kwargs['pk']
            lobby = Lobby.load(name)
            serializer = LobbySerializer(lobby)
            return serializer.data
        except KeyError:
            raise Http404()

    def delete(self, request, *args, **kwargs):
        name = self.kwargs['pk']
        try:
            lobby = Lobby.load(name)
            lobby.delete()
            players = Player.query(Player.lobby == name)
            for player in players:
                player.delete()

            lobby_deleted.send(LobbyDetailsView, data=name)
            return Response(name, status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            raise Http404()


class NewGameView(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        payload = {
            'game_id': request.data['game_id'],
            'players': request.data['players'],
        }
        serialized = GameInstanceSerializer(data=payload)
        serialized.is_valid()
        instance = serialized.save()
        game_instance_id = instance.public_id
        response = {
            'lobby': self.kwargs['pk'],
            'game_instance_id': str(game_instance_id)
        }

        game_created.send(NewGameView, data=response)

        return Response(game_instance_id, status=status.HTTP_201_CREATED)
