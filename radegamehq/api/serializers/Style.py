from rest_framework import serializers

from ..entities.Style import Style


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
