from rest_framework import generics

from api.entities.Phase import Phase
from api.serializers.Phase import PhaseSerializer


class PhaseView(generics.ListCreateAPIView):
    serializer_class = PhaseSerializer

    def get_queryset(self):
        return Phase.objects.all().filter(game=self.kwargs['pk'])


class PhaseDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhaseSerializer

    def get_queryset(self):
        return Phase.objects.all()
