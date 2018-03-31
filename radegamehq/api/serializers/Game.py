from rest_framework import serializers

from api.entities.Game import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'image', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')