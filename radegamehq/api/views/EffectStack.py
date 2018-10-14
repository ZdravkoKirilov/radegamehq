from rest_framework import generics

from api.entities.EffectStack import EffectStack
from api.serializers.EffectStack import EffectStackSerializer


class EffectStackView(generics.ListCreateAPIView):
    serializer_class = EffectStackSerializer

    def get_queryset(self):
        return EffectStack.objects.all().filter(game=self.kwargs['pk'])


class EffectStackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EffectStackSerializer
    queryset = EffectStack.objects.all()
