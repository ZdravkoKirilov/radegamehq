from rest_framework import serializers
from ..entities.Token import Token

from ..entities.Condition import Condition

from ..mixins.NestedSerializing import NestedSerializer


class TokenSerializer(NestedSerializer, serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'restricted', 'model': Condition, 'm2m': True},
            {'name': 'allowed', 'model': Condition, 'm2m': True},
        ]
