from rest_framework import generics
from .serializers import GameSerializer, BoardFieldSerializer, MapLocationSerializer, MapPathSerializer, \
    ResourceSerializer, FactionSerializer, ActivitySerializer, QuestSerializer, RoundSerializer, TriviaSerializer, \
    StageSerializer
from .models import Game, BoardField, MapLocation, MapPath, Resource, Faction, Round, Activity, Quest, Trivia, \
    Stage


class GameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class RoundView(generics.ListCreateAPIView):
    serializer_class = RoundSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Round.objects.all().filter(game=self.kwargs['pk'])


class RoundDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoundSerializer

    def get_queryset(self):
        return Round.objects.all()


class QuestView(generics.ListCreateAPIView):
    serializer_class = QuestSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Quest.objects.all().filter(game=self.kwargs['pk'])


class QuestDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestSerializer

    def get_queryset(self):
        return Quest.objects.all()


class ActivityView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Activity.objects.all().filter(game=self.kwargs['pk'])


class ActivityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.all()


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


class TriviaView(generics.ListCreateAPIView):
    serializer_class = TriviaSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Trivia.objects.all().filter(game=self.kwargs['pk'])


class TriviaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TriviaSerializer

    def get_queryset(self):
        return Trivia.objects.all()


class StageView(generics.ListCreateAPIView):
    serializer_class = StageSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Stage.objects.all().filter(game=self.kwargs['pk'])


class StageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StageSerializer

    def get_queryset(self):
        return Stage.objects.all()
