from rest_framework import generics

from ..entities.State import State
from ..serializers.State import StateSerializer


class StateView(generics.ListCreateAPIView):
    serializer_class = StateSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return State.objects.all().filter(game=self.kwargs['pk'])


class StateDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return State.objects.all()
