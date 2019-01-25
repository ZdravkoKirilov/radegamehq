from rest_framework import serializers

from ..entities.Stage import Stage
from ..helpers.image_sanitize import sanitize_image


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = '__all__'

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(StageSerializer, self).to_internal_value(data)
        return value
