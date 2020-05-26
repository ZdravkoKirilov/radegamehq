from rest_framework import generics

from ..entities.Sandbox import Sandbox
from ..serializers.Sandbox import SandboxSerializer


class SandboxView(generics.ListCreateAPIView):
    serializer_class = SandboxSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Sandbox.objects.all().filter(game=self.kwargs['pk'])


class SandboxDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SandboxSerializer

    def get_queryset(self):
        return Sandbox.objects.all()
