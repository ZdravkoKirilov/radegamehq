from rest_framework import generics

from ..entities.Action import Action
from ..serializers.Action import ActionSerializer


class ActionView(generics.ListCreateAPIView):
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all().filter(game=self.kwargs['pk'])


class ActionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all()
