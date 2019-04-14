from rest_framework import serializers

from ..entities.Style import Style
from ..entities.Keyword import Keyword
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
