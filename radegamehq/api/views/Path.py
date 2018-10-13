from rest_framework import generics

from api.entities.Path import Path
from api.serializers.Path import MapPathSerializer


class MapPathView(generics.ListCreateAPIView):
    serializer_class = MapPathSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Path.objects.all().filter(game=self.kwargs['pk'])


class MapPathDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MapPathSerializer

    def get_queryset(self):
        return Path.objects.all()