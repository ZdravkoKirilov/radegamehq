from rest_framework import serializers

from ..entities.Slot import Slot, SlotItem, SlotHandler
from ..mixins.NestedSerializing import with_nesting


class SlotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotItem
        fields = '__all__'


class SlotHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotHandler
        fields = '__all__'


@with_nesting([
    {'name': 'items', 'model': SlotItem, 'm2m': False, 'serializer': SlotItemSerializer},
    {'name': 'handlers', 'model': SlotHandler, 'm2m': False, 'serializer': SlotHandlerSerializer},
])
class SlotSerializer(serializers.ModelSerializer):
    items = SlotItemSerializer(many=True)
    handlers = SlotHandlerSerializer(many=True)

    class Meta:
        model = Slot
        fields = '__all__'
