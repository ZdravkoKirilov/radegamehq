from rest_framework import generics

from api.entities.Round import Round
from api.serializers.Round import RoundSerializer


class RoundView(generics.ListCreateAPIView):
    serializer_class = RoundSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Round.objects.all().filter(game=self.kwargs['pk'])


class RoundDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoundSerializer

    def get_queryset(self):
        return Round.objects.all()