from rest_framework import generics

from ..entities.Version import Version
from ..serializers.Version import VersionSerializer


class VersionView(generics.ListCreateAPIView):
    serializer_class = VersionSerializer

    def get_queryset(self):
        return Version.objects.all().filter(game=self.kwargs['pk'])


class VersionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VersionSerializer

    def get_queryset(self):
        return Version.objects.all()