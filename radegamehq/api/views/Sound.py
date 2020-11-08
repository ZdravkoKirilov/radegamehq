from rest_framework import generics

from ..entities.Sound import Sound
from ..serializers.Sound import SoundSerializer


class SoundView(generics.ListCreateAPIView):
    serializer_class = SoundSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Sound.objects.all().filter(module=self.kwargs['moduleid'])


class SoundDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SoundSerializer

    def get_queryset(self):
        return Sound.objects.all()
