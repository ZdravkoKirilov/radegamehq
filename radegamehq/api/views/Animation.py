from rest_framework import generics

from ..entities.Animation import Animation
from ..serializers.Animation import AnimationSerializer


class AnimationView(generics.ListCreateAPIView):
    serializer_class = AnimationSerializer

    def get_queryset(self):
        return Animation.objects.all().filter(module=self.kwargs['moduleid'])


class AnimationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimationSerializer

    def get_queryset(self):
        return Animation.objects.all()
