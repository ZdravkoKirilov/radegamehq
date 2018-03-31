from rest_framework import generics

from api.entities.Location import MapLocation
from api.serializers.Location import MapLocationSerializer


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