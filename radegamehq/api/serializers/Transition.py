from rest_framework import serializers

from ..entities.Transition import Transition


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = '__all__'
