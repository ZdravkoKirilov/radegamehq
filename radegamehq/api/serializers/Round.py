from rest_framework import serializers

from ..entities.Round import Round
from ..entities.Source import Source
from ..entities.Phase import Phase
from ..entities.Condition import Condition
from ..helpers.image_sanitize import sanitize_image
from ..mixins.NestedSerializing import NestedSerializer


class RoundSerializer(NestedSerializer, serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'condition', 'model': Condition, 'm2m': True},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
            {'name': 'phases', 'model': Phase, 'm2m': True}
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(RoundSerializer, self).to_internal_value(data)
        return value
