from rest_framework import serializers

from ..entities.Choice import ChoiceOption, Choice
from ..entities.Source import Source
from ..entities.Condition import Condition

from ..helpers.image_sanitize import sanitize_image
from ..mixins.NestedSerializing import NestedSerializer


class ChoiceOptionSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

    def nested_entities(self):
        return [
            {'name': 'effect', 'model': Source, 'm2m': True},
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
            {'name': 'cost', 'model': Source, 'm2m': True},
            {'name': 'condition', 'model': Condition, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
            {'name': 'reveal_cost', 'model': Source, 'm2m': True},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
        ]

    class Meta:
        model = Choice
        fields = '__all__'
