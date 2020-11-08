from rest_framework import generics

from ..entities.Setup import Setup
from ..serializers.Setup import SetupSerializer


class SetupView(generics.ListCreateAPIView):
    serializer_class = SetupSerializer

    def get_queryset(self):
        return Setup.objects.all().filter(version=self.kwargs['versionid'])


class SetupDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SetupSerializer

    def get_queryset(self):
        return Setup.objects.all()
