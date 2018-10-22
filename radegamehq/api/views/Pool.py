from rest_framework import generics

from api.entities.Pool import Pool
from api.serializers.Pool import PoolSerializer


class PoolView(generics.ListCreateAPIView):
    serializer_class = PoolSerializer

    def get_queryset(self):
        return Pool.objects.all().filter(game=self.kwargs['pk'])


class PoolDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PoolSerializer
    queryset = Pool.objects.all()
