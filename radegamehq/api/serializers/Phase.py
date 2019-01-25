from rest_framework import serializers
from ..entities.Phase import Phase

from ..helpers.image_sanitize import sanitize_image


class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = '__all__'

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(PhaseSerializer, self).to_internal_value(data)
        return value
