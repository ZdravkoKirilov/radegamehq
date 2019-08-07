from rest_framework import serializers

from ..entities.Stage import Stage


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
