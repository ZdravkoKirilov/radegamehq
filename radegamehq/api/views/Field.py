from rest_framework import generics

from api.entities.Field import Field
from api.serializers.Field import BoardFieldSerializer


class BoardFieldView(generics.ListCreateAPIView):
    serializer_class = BoardFieldSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Field.objects.all().filter(game=self.kwargs['pk'])


class BoardFieldDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardFieldSerializer

    def get_queryset(self):
        return Field.objects.all()