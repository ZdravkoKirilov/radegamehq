from rest_framework import serializers
from ..entities.Setup import Setup


class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setup
        fields = '__all__'
