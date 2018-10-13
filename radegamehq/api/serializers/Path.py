from rest_framework import serializers

from api.entities.Path import Path


class MapPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ('id', 'game', 'stage', 'from_loc', 'to_loc')