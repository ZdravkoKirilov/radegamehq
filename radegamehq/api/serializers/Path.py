from rest_framework import serializers

from api.entities.Path import MapPath


class MapPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPath
        fields = ('id', 'game', 'stage', 'fromLoc', 'toLoc')
        read_only_fields = ('date_created', 'date_modified')