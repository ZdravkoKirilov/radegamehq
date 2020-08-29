from rest_framework.serializers import ModelSerializer

from ..helpers.image_sanitize import sanitize_image

class ImageHandler(ModelSerializer):

    class Meta:
        abstract = True

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super().to_internal_value(data)
        return value
