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



