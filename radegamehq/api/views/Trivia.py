from rest_framework import generics

from api.entities.Choice import Choice
from api.serializers.Choice import ChoiceSerializer


class TriviaView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Choice.objects.all().filter(game=self.kwargs['pk'])


class TriviaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return Choice.objects.all()