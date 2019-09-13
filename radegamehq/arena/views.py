from rest_framework import generics, status
from rest_framework.response import Response
from .models import GameInstance
from .serializers import GameInstanceSerializer


class GameInstanceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameInstanceSerializer

    def get_queryset(self):
        try:
            return GameInstance.objects.get(public_id=self.kwargs['public_id'])
        except GameInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ActiveGamesView(generics.ListAPIView):
    serializer_class = GameInstanceSerializer

    def get_queryset(self):
        result = GameInstance.objects.filter(players__user_id=self.kwargs['user_id'])
        return result
