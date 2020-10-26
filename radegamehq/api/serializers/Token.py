from rest_framework import serializers

from ..entities.Token import Token, TokenNode
from ..mixins.NestedSerializing import with_nesting


class TokenNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenNode
        fields = '__all__'


@with_nesting([
    {'name': 'nodes', 'model': TokenNode, 'm2m': False, 'serializer': TokenNodeSerializer},
])
class TokenSerializer(serializers.ModelSerializer):
    nodes = TokenNodeSerializer(many=True)

    class Meta:
        model = Token
        fields = '__all__'
