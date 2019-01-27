from rest_framework import serializers
from ..entities.Phase import Phase

from ..helpers.image_sanitize import sanitize_image


class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = '__all__'

