from api.helpers.image_sanitize import sanitize_image
from rest_framework.serializers import ModelSerializer


class ImageHandler:
    @property
    def converter(self):
        raise NotImplementedError

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = ModelSerializer(self.converter(), self).to_internal_value(data)
        return value
