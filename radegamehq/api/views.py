from rest_framework import generics
from .serializers import GameSerializer, BoardFieldSerializer, MapLocationSerializer, MapSerializer, MapPathSerializer, \
    ResourceSerializer, FactionSerializer, ActionSerializer
from .models import Game, BoardField, MapLocation, Map, MapPath, Resource, Faction, Action


class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ActionView(generics.ListCreateAPIView):
    serializer_class = ActionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Action.objects.all().filter(game=self.kwargs['pk'])


class ActionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all()


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


class MapPathView(generics.ListCreateAPIView):
    serializer_class = MapPathSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return MapPath.objects.all().filter(game=self.kwargs['pk'])


class MapPathDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MapPathSerializer

    def get_queryset(self):
        return MapPath.objects.all()


class ResourceView(generics.ListCreateAPIView):
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Resource.objects.all().filter(game=self.kwargs['pk'])


class ResourceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceSerializer

    def get_queryset(self):
        return Resource.objects.all()


class FactionView(generics.ListCreateAPIView):
    serializer_class = FactionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Faction.objects.all().filter(game=self.kwargs['pk'])


class FactionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FactionSerializer

    def get_queryset(self):
        return Faction.objects.all()
