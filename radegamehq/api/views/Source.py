from rest_framework import generics

from api.entities.Source import Source
from api.serializers.Source import SourceSerializer


class SourceView(generics.ListCreateAPIView):
    serializer_class = SourceSerializer

    def get_queryset(self):
        return Source.objects.all().filter(game=self.kwargs['pk'])


class SourceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
