from .models import Lobby, Player
from .serializers import LobbySerializer, PlayerSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404

from .signals import lobby_created


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

    # def on_lobby_created(self):
    #     lobby_created.connect(LobbyListView.pesho)
    #
    # @staticmethod
    # def pesho(sender=Lobby, **kwargs):
    #     pass


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
        lobby = Lobby.load(name)
        lobby.delete()
