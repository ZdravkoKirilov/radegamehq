from rest_framework import serializers

from ..entities.Choice import ChoiceOption, Choice

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField
from ..mixins.NestedSerializing import NestedSerializer
from ..entities.Stack import Stack


class ChoiceOptionSerializer(NestedSerializer, serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)
    image = Base64ImageField(max_length=None, use_url=True, required=False, validators=[])

    def nested_entities(self):
        return [
            {'name': 'effect', 'model': Stack, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ChoiceOptionSerializer, self).to_internal_value(data)
        return value

    class Meta:
        model = ChoiceOption
        fields = ('id', 'name', 'description', 'keywords', 'image', 'effect')


class ChoiceSerializer(NestedSerializer, serializers.ModelSerializer):
    options = ChoiceOptionSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True, required=False, validators=[])

    def nested_entities(self):
        return [
            {'name': 'options', 'model': ChoiceOption, 'm2m': False, 'serializer': ChoiceOptionSerializer},
            {'name': 'cost', 'model': Stack, 'm2m': True},
            {'name': 'condition', 'model': Stack, 'm2m': True},
            {'name': 'restricted', 'model': Stack, 'm2m': True},
            {'name': 'allowed', 'model': Stack, 'm2m': True},
        ]

    class Meta:
        model = Choice
        fields = (
            'id', 'game', 'mode', 'name', 'description', 'image', 'options', 'keywords', 'cost', 'condition',
            'restricted', 'allowed')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        # for item in data['options']:
        #     sanitize_image(item)
        value = super(ChoiceSerializer, self).to_internal_value(data)
        return value
