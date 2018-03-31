from rest_framework import generics

from api.entities.Faction import Faction
from api.serializers.Faction import FactionSerializer


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