from rest_framework import serializers

from ..entities.Sound import Sound


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = '__all__'
