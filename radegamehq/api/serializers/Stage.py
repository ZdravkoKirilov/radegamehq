from rest_framework import serializers

from ..entities.Stage import Stage
from ..helpers.image_sanitize import sanitize_image


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = '__all__'


