from rest_framework import generics

from api.entities.EffectGroup import EffectGroup
from api.serializers.EffectGroup import EffectGroupSerializer


class EffectGroupView(generics.ListCreateAPIView):
    serializer_class = EffectGroupSerializer

    def get_queryset(self):
        return EffectGroup.objects.all().filter(game=self.kwargs['pk'])


class EffectGroupDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EffectGroupSerializer
    queryset = EffectGroup.objects.all()
