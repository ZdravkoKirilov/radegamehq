from rest_framework import serializers

from ..entities.Choice import ChoiceOption, Choice
from ..entities.Condition import Condition

from ..mixins.NestedSerializing import NestedSerializer


class ChoiceOptionSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    def nested_entities(self):
        return [
            {'name': 'settings', 'model': Condition, 'm2m': True},
        ]

    class Meta:
        model = ChoiceOption
        fields = '__all__'


class ChoiceSerializer(NestedSerializer, serializers.ModelSerializer):
    options = ChoiceOptionSerializer(many=True)

    def nested_entities(self):
        return [
            {'name': 'options', 'model': ChoiceOption, 'm2m': False, 'serializer': ChoiceOptionSerializer},
            {'name': 'condition', 'model': Condition, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
        ]

    class Meta:
        model = Choice
        fields = '__all__'
