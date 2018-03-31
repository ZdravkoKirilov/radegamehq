from rest_framework import generics

from api.entities.Game import Game
from api.serializers.Game import GameSerializer


class GameView(generics.ListCreateAPIView):
    serializer_class = GameSerializer

    ##permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get_queryset(self):
        user = self.request.user
        queryset = Game.objects.filter(owner=user.id)
        return queryset


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer