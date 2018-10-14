from rest_framework import generics

from api.entities.Choice import Choice
from api.serializers.Choice import ChoiceSerializer


class ChoiceView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return Choice.objects.all().filter(game=self.kwargs['pk'])


class ChoiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return Choice.objects.all()