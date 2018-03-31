from rest_framework import generics

from api.entities.Resource import Resource
from api.serializers.Resource import ResourceSerializer


class ResourceView(generics.ListCreateAPIView):
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Resource.objects.all().filter(game=self.kwargs['pk'])


class ResourceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceSerializer

    def get_queryset(self):
        return Resource.objects.all()