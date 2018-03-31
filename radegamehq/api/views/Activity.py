from rest_framework import generics

from api.entities.Activity import Activity
from api.serializers.Activity import ActivitySerializer


class ActivityView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Activity.objects.all().filter(game=self.kwargs['pk'])


class ActivityDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.all()