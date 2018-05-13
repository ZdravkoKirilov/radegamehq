from rest_framework import serializers

from api.entities.Location import MapLocation


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = ('id', 'width', 'height', 'y', 'x', 'game', 'stage', 'field')
        read_only_fields = ('date_created', 'date_modified')