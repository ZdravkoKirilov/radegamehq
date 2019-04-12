from rest_framework import generics

from ..entities.Keyword import Keyword
from ..serializers.Keyword import KeywordSerializer


class KeywordView(generics.ListCreateAPIView):
    serializer_class = KeywordSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Keyword.objects.all().filter(game=self.kwargs['pk'])


class KeywordDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KeywordSerializer

    def get_queryset(self):
        return Keyword.objects.all()
