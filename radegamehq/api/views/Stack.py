from rest_framework import generics

from api.entities.Stack import EffectStack
from api.serializers.Stack import StackSerializer


class StackView(generics.ListCreateAPIView):
    serializer_class = StackSerializer

    def get_queryset(self):
        return EffectStack.objects.all().filter(game=self.kwargs['pk'])


class StackDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StackSerializer
    queryset = EffectStack.objects.all()
