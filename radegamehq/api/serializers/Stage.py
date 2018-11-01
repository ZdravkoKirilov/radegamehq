from rest_framework import serializers

from ..entities.Stage import Stage
from ..helpers.image_sanitize import sanitize_image


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'name', 'description', 'image', 'game')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(StageSerializer, self).to_internal_value(data)
        return value
