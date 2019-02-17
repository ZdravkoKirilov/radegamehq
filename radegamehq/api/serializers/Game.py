from rest_framework import serializers

from ..entities.Game import Game, Setup
from ..entities.Condition import Condition
from ..mixins.NestedSerializing import with_nesting
from .custom_serializers import Base64ImageField
from ..helpers.image_sanitize import sanitize_image


@with_nesting([
    {'name': 'settings', 'model': Condition, 'm2m': True},
])
class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setup
        fields = '__all__'


@with_nesting([
    {'name': 'setups', 'model': Setup, 'm2m': False, 'serializer': SetupSerializer}
])
class GameSerializer(serializers.ModelSerializer):
    image = Base64ImageField(use_url=True)
    setups = SetupSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
