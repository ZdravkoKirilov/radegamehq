from rest_framework import generics

from ..entities.ImageAsset import ImageAsset
from ..serializers.ImageAsset import ImageAssetSerializer


class ImageAssetView(generics.ListCreateAPIView):
    serializer_class = ImageAssetSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return ImageAsset.objects.all().filter(game=self.kwargs['pk'])


class ImageAssetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageAssetSerializer

    def get_queryset(self):
        return ImageAsset.objects.all()
