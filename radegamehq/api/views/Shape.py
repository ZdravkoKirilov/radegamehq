from rest_framework import generics

from ..entities.Shape import Shape
from ..serializers.Shape import ShapeSerializer


class ShapeView(generics.ListCreateAPIView):
    serializer_class = ShapeSerializer

    def get_queryset(self):
        return Shape.objects.all().filter(module=self.kwargs['moduleid'])


class ShapeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShapeSerializer

    def get_queryset(self):
        return Shape.objects.all()