from rest_framework import generics

from api.entities.Module import Module
from api.serializers.Module import ModuleSerializer


class ModuleView(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Module.objects.all().filter(game=self.kwargs['pk'])


class ModuleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.all()