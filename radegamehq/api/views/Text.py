from rest_framework import generics

from ..entities.Text import Text
from ..serializers.Text import TextSerializer


class TextView(generics.ListCreateAPIView):
    serializer_class = TextSerializer

    def get_queryset(self):
        return Text.objects.all().filter(game=self.kwargs['pk'])


class TextDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TextSerializer

    def get_queryset(self):
        return Text.objects.all()