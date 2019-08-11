from rest_framework import generics

from ..entities.Handler import Handler
from ..serializers.Handler import HandlerSerializer


class HandlerView(generics.ListCreateAPIView):
    serializer_class = HandlerSerializer

    def get_queryset(self):
        return Handler.objects.all().filter(game=self.kwargs['pk'])


class HandlerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HandlerSerializer

    def get_queryset(self):
        return Handler.objects.all()
