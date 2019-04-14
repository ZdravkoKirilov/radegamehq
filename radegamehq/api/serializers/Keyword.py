from rest_framework import serializers

from ..entities.Keyword import Keyword
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
