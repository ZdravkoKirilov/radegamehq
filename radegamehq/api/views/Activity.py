from rest_framework import generics

from api.entities.Action import Action
from api.serializers.Action import ActionSerializer


class ActivityView(generics.ListCreateAPIView):
    serializer_class = ActionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Action.objects.all().filter(game=self.kwargs['pk'])


class ActivityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all()