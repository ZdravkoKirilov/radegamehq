from rest_framework import serializers

from api.entities.Location import Location


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'game', 'stage', 'field',  'width', 'height', 'y', 'x',)
