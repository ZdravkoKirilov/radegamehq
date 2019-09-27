from rest_framework import generics

from ..entities.Transition import Transition
from ..serializers.Transition import TransitionSerializer


class TransitionView(generics.ListCreateAPIView):
    serializer_class = TransitionSerializer

    def get_queryset(self):
        return Transition.objects.all().filter(game=self.kwargs['pk'])


class TransitionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransitionSerializer

    def get_queryset(self):
        return Transition.objects.all()
