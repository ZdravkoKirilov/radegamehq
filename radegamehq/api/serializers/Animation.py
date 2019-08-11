from rest_framework import serializers

from ..entities.Animation import Animation


class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animation
        fields = '__all__'
