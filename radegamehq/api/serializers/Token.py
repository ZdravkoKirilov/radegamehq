from rest_framework import serializers

from ..entities.Token import Token
from ..entities.Keyword import Keyword
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
