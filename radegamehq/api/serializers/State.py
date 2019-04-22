from rest_framework import serializers

from ..entities.State import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
