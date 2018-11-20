from rest_framework import generics

from api.entities.Slot import Slot
from api.serializers.Slot import SlotSerializer


class SlotView(generics.ListCreateAPIView):
    serializer_class = SlotSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Slot.objects.all()


class SlotDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SlotSerializer

    def get_queryset(self):
        return Slot.objects.all()