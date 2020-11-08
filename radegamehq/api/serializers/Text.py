from rest_framework import serializers

from ..entities.Text import Text, Translation
from ..mixins.NestedSerializing import with_nesting


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'


@with_nesting([
    {'name': 'translations', 'model': Translation, 'm2m': False, 'serializer': TranslationSerializer},
])
class TextSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True, allow_null=True, allow_empty=True, default=[])

    class Meta:
        model = Text
        fields = '__all__'
