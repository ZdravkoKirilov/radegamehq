from rest_framework import generics

from api.entities.Trivia import Trivia
from api.serializers.Trivia import TriviaSerializer


class TriviaView(generics.ListCreateAPIView):
    serializer_class = TriviaSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Trivia.objects.all().filter(game=self.kwargs['pk'])


class TriviaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TriviaSerializer

    def get_queryset(self):
        return Trivia.objects.all()