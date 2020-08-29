from rest_framework import serializers
from ..entities.Version import Version


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'