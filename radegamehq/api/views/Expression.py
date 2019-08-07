from rest_framework import generics

from ..entities.Expression import Expression
from ..serializers.Expression import ExpressionSerializer


class ExpressionView(generics.ListCreateAPIView):
    serializer_class = ExpressionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Expression.objects.all().filter(game=self.kwargs['pk'])


class ExpressionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpressionSerializer

    def get_queryset(self):
        return Expression.objects.all()
