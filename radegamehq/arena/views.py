from django.db.models import QuerySet
from rest_framework import generics
from .models import GameInstance
from .serializers import GameInstanceSerializer


class GameInstanceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameInstanceSerializer
    lookup_field = 'public_id'

    def get_queryset(self) -> QuerySet:
        return GameInstance.objects.all()


class ActiveGamesView(generics.ListAPIView):
    serializer_class = GameInstanceSerializer

    def get_queryset(self):
        result = GameInstance.objects.filter(players__user_id=self.kwargs['user_id'])
        return result
