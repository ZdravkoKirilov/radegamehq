from rest_framework import generics

from api.entities.Condition import Condition
from api.serializers.Condition import QuestSerializer


class QuestView(generics.ListCreateAPIView):
    serializer_class = QuestSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Condition.objects.all().filter(game=self.kwargs['pk'])


class QuestDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestSerializer

    def get_queryset(self):
        return Condition.objects.all()