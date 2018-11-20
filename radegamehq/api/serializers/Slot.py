from rest_framework import serializers

from ..entities.Slot import Slot
from ..entities.Condition import Condition
from ..mixins.NestedSerializing import NestedSerializer
from ..helpers.image_sanitize import sanitize_image
from ..entities.Token import Token
from .custom_serializers import Base64ImageField


class SlotSerializer(NestedSerializer, serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Slot
        fields = (
            'id', 'game', 'owner', 'name', 'description', 'image', 'keywords', 'field', 'tokens', 'width', 'height',
            'y', 'x', 'allowed', 'restricted')

    def nested_entities(self):
        return [
            {'name': 'allowed', 'model': Condition, 'm2m': True},
            {'name': 'restricted', 'model': Condition, 'm2m': True},
            {'name': 'tokens', 'model': Token, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(SlotSerializer, self).to_internal_value(data)
        return value
