from rest_framework import serializers

from ..entities.Sandbox import Sandbox


class SandboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandbox
        fields = '__all__'
