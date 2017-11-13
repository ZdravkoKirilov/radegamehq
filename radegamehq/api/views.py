from rest_framework import generics
from .serializers import GameSerializer, BoardFieldSerializer, MapLocationSerializer, MapSerializer
from .models import Game, BoardField, MapLocation, Map


class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class BoardFieldView(generics.ListCreateAPIView):
    serializer_class = BoardFieldSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return BoardField.objects.all().filter(game=self.kwargs['pk'])


class BoardFieldDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardFieldSerializer

    def get_queryset(self):
        return BoardField.objects.all()


class MapLocationView(generics.ListCreateAPIView):
    serializer_class = MapLocationSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return MapLocation.objects.all()


class MapLocationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MapLocationSerializer

    def get_queryset(self):
        return MapLocation.objects.all()


class MapView(generics.ListCreateAPIView):
    serializer_class = MapSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Map.objects.all().filter(game=self.kwargs['pk'])


class MapDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MapSerializer

    def get_queryset(self):
        return Map.objects.all()
