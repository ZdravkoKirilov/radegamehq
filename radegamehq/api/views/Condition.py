from rest_framework import generics

from api.entities.Condition import Condition
from api.serializers.Condition import ConditionSerializer


class ConditionView(generics.ListCreateAPIView):
    serializer_class = ConditionSerializer

    def get_queryset(self):
        return Condition.objects.all().filter(game=self.kwargs['pk'])


class ConditionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConditionSerializer

    def get_queryset(self):
        return Condition.objects.all()