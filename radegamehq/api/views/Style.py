from rest_framework import generics

from ..entities.Style import Style
from ..serializers.Style import StyleSerializer


class StyleView(generics.ListCreateAPIView):
    serializer_class = StyleSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Style.objects.all().filter(module=self.kwargs['moduleid'])


class StyleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StyleSerializer

    def get_queryset(self):
        return Style.objects.all()
