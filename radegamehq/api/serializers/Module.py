from rest_framework import serializers

from ..entities.Module import Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
