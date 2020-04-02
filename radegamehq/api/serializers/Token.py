from rest_framework import serializers

from ..entities.Token import Token, TokenFrame, TokenText
from ..mixins.NestedSerializing import with_nesting


class TokenFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenFrame
        fields = '__all__'


class TokenTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenText
        fields = '__all__'


@with_nesting([
    {'name': 'frames', 'model': TokenFrame, 'm2m': False, 'serializer': TokenFrameSerializer},
    {'name': 'texts', 'model': TokenText, 'm2m': False, 'serializer': TokenTextSerializer},
])
class TokenSerializer(serializers.ModelSerializer):
    frames = TokenFrameSerializer(many=True)
    texts = TokenTextSerializer(many=True)

    class Meta:
        model = Token
        fields = '__all__'
