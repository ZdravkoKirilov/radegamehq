from rest_framework import serializers

from ..entities.Faction import Faction


class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = '__all__'
