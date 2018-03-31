from rest_framework import generics

from api.entities.Stage import Stage
from api.serializers.Stage import StageSerializer


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