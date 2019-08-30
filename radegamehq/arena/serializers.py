from rest_framework import serializers

from .models import GameInstance, GamePlayer
from api.mixins.NestedSerializing import with_nesting


class GamePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlayer
        fields = '__all__'


@with_nesting([
    {'name': 'players', 'model': GamePlayer, 'm2m': False, 'serializer': GamePlayerSerializer},
])
class GameInstanceSerializer(serializers.ModelSerializer):
    players = GamePlayerSerializer(many=True)
    
    class Meta:
        model = GameInstance
        fields = '__all__'
