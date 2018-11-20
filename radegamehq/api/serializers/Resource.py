from rest_framework import serializers

from api.entities.Slot import Slot
from api.helpers.image_sanitize import sanitize_image


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id', 'name', 'description', 'keywords', 'image', 'game')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ResourceSerializer, self).to_internal_value(data)
        return value
