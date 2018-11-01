from rest_framework import generics

from api.entities.Team import Team
from api.serializers.Team import TeamSerializer


class TeamView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all().filter(game=self.kwargs['pk'])


class TeamDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()