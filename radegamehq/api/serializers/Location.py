from rest_framework import serializers

from api.entities.Location import Location


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'width', 'height', 'y', 'x', 'game', 'stage', 'field')
