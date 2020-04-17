from django.db.models import QuerySet
from rest_framework import generics

from api.entities.Stage import Stage, Slot
from api.serializers.Stage import StageSerializer, SlotSerializer


class StageView(generics.ListCreateAPIView):
    serializer_class = StageSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Stage.objects.all().filter(game=self.kwargs['pk'])


class StageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StageSerializer

    def get_queryset(self):
        return Stage.objects.all()


class SlotView(generics.ListCreateAPIView):
    serializer_class = SlotSerializer

    def perform_create(self, serializer: SlotSerializer) -> None:
        serializer.save()

    def get_queryset(self) -> QuerySet:
        return Slot.objects.all().filter(owner=self.kwargs['stageId'])


class SlotDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SlotSerializer

    def get_queryset(self) -> QuerySet:
        return Slot.objects.all()
