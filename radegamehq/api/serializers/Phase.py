from rest_framework import serializers
from ..entities.Phase import Phase


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'
