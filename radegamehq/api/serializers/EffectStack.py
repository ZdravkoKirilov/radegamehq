from rest_framework import serializers

from api.entities.EffectStack import EffectStack


class EffectStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectStack
        fields = ('id', 'action', 'condition', 'relation')
