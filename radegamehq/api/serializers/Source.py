from rest_framework import serializers

from ..entities.Source import Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
