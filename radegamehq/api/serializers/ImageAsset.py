from typing import Any

from ..entities.ImageAsset import ImageAsset
from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField


class ImageAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset
        fields = '__all__'

    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )

    image = HyperlinkedSorlImageField('1024')

    def to_internal_value(self, data):
        image = data['image']
        if image is not None and type(image) == str and image.startswith('http'):
            data.pop('image')
        return super().to_internal_value(data)


    def to_representation(self, instance: Any) -> Any:
        representation = super().to_representation(instance)
        image: str = representation['image']
        thumbnail = representation['thumbnail']
        if image is not None and not image.startswith('http'):
            representation['image'] = 'http://localhost:8000' + image
        if thumbnail is not None and not thumbnail.startswith('http'):
            representation['thumbnail'] = 'http://localhost:8000' + thumbnail
        return representation
