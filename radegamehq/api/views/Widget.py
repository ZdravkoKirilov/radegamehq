from django.db.models import QuerySet
from rest_framework import generics

from api.entities.Widget import Widget, WidgetNode
from api.serializers.Widget import WidgetSerializer, NodeSerializer


class WidgetView(generics.ListCreateAPIView):
    serializer_class = WidgetSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Widget.objects.all().filter(game=self.kwargs['pk'])


class WidgetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WidgetSerializer

    def get_queryset(self):
        return Widget.objects.all()


class NodeView(generics.ListCreateAPIView):
    serializer_class = NodeSerializer

    def perform_create(self, serializer: NodeSerializer) -> None:
        serializer.save()

    def get_queryset(self) -> QuerySet:
        return WidgetNode.objects.all().filter(owner=self.kwargs['widgetId'])


class NodeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self) -> QuerySet:
        return WidgetNode.objects.all()
