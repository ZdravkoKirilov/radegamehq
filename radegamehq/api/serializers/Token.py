from rest_framework import serializers

from ..entities.Token import Token, TokenFrame
from ..mixins.NestedSerializing import with_nesting


class TokenFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenFrame
        fields = '__all__'


@with_nesting([
    {'name': 'frames', 'model': TokenFrame, 'm2m': False, 'serializer': TokenFrameSerializer}
])
class TokenSerializer(serializers.ModelSerializer):
    frames = TokenFrameSerializer(many=True)

    class Meta:
        model = Token
        fields = '__all__'
