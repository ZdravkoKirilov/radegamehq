from rest_framework import serializers

from ..entities.Game import Game
from .custom_serializers import Base64ImageField


class GameSerializer(serializers.ModelSerializer):
    image = Base64ImageField(use_url=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
