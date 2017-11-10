from rest_framework import generics
from .serializers import GameSerializer, BoardFieldSerializer
from .models import Game, BoardField


class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class BoardFieldView(generics.ListCreateAPIView):
    queryset = BoardField.objects.all()
    serializer_class = BoardFieldSerializer

    def perform_create(self, serializer):
        serializer.save()


class BoardFieldDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardField.objects.all()
    serializer_class = BoardFieldSerializer
