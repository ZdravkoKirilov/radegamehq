from rest_framework import serializers

from ..entities.Field import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
