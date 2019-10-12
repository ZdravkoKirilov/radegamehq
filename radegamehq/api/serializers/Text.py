from rest_framework import serializers

from ..entities.Text import Text, Translation
from ..entities.Keyword import Keyword
from ..mixins.NestedSerializing import with_nesting


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'


@with_nesting([
    {'name': 'translations', 'model': Translation, 'm2m': False, 'serializer': TranslationSerializer},
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class TextSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True)

    class Meta:
        model = Text
        fields = '__all__'
