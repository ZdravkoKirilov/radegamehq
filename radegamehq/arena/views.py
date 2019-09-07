from rest_framework import generics

from .models import GameInstance
from .serializers import GameInstanceSerializer


class GameInstanceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameInstanceSerializer

    def get_queryset(self):
        return GameInstance.objects.all().filter(public_id=self.kwargs['public_id'])


class ActiveGamesView(generics.RetrieveAPIView):
    serializer_class = GameInstanceSerializer

    def get_queryset(self):
        return GameInstance.objects.all().filter(public_id=self.kwargs['public_id'])
