from rest_framework import serializers

from api.entities.Game import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
