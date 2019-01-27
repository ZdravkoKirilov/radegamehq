from ..entities.ImageAsset import ImageAsset
from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField


class ImageAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageAsset
        fields = ('image', 'id', 'name', 'thumbnail', 'svg', 'game')

    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )

    image = HyperlinkedSorlImageField('1024')
    game = serializers.PrimaryKeyRelatedField(read_only=True)
