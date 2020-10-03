from rest_framework import serializers

from ..entities.Game import Game, GameLanguage
from .custom_serializers import Base64ImageField
from ..mixins.NestedSerializing import with_nesting
from ..mixins.ImageHandler import ImageHandler


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLanguage
        fields = '__all__'


@with_nesting([
    {'name': 'languages', 'model': GameLanguage, 'm2m': False, 'serializer': LanguageSerializer},
])
class GameSerializer(ImageHandler):
    image = Base64ImageField(use_url=True)
    languages = LanguageSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
