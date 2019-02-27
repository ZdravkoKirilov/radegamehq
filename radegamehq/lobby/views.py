from .models import Lobby, Player
from .serializers import LobbySerializer, PlayerSerializer
from rest_framework import generics
from django.http import Http404


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
        player.delete()


class LobbyListView(generics.ListCreateAPIView):
    serializer_class = LobbySerializer

    def get_queryset(self):
        lobbies = Lobby.all()
        items = [item for item in lobbies]
        return items


class LobbyDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class = LobbySerializer

    def get_object(self):
        name = self.kwargs['pk']
        lobby = Lobby.load(name)
        serializer = LobbySerializer(lobby)
        return serializer.data

    def delete(self, request, *args, **kwargs):
        name = self.kwargs['pk']
        lobby = Lobby.load(name)
        lobby.delete()
