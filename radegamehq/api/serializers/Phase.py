from rest_framework import serializers
from ..entities.Phase import Phase

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField


class PhaseSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Phase
        fields = ('id', 'game', 'name', 'description', 'image', 'keywords')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(PhaseSerializer, self).to_internal_value(data)
        return value
