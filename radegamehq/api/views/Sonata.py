from rest_framework import generics

from ..entities.Sonata import Sonata
from ..serializers.Sonata import SonataSerializer


class SonataView(generics.ListCreateAPIView):
    serializer_class = SonataSerializer

    def get_queryset(self):
        return Sonata.objects.all().filter(module=self.kwargs['moduleid'])


class SonataDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SonataSerializer

    def get_queryset(self):
        return Sonata.objects.all()