from rest_framework import serializers

from ..entities.Slot import Slot, SlotItem, SlotHandler, SlotFrame
from ..entities.Transition import Transition
from ..mixins.NestedSerializing import with_nesting


class SlotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotItem
        fields = '__all__'


class SlotHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotHandler
        fields = '__all__'


class SlotFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotFrame
        fields = '__all__'


@with_nesting([
    {'name': 'items', 'model': SlotItem, 'm2m': False, 'serializer': SlotItemSerializer},
    {'name': 'handlers', 'model': SlotHandler, 'm2m': False, 'serializer': SlotHandlerSerializer},
    {'name': 'transitions', 'model': Transition, 'm2m': True},
    {'name': 'frames', 'model': SlotFrame, 'm2m': False, 'serializer': SlotFrameSerializer},
])
class SlotSerializer(serializers.ModelSerializer):
    items = SlotItemSerializer(many=True)
    handlers = SlotHandlerSerializer(many=True)
    frames = SlotFrameSerializer(many=True)

    class Meta:
        model = Slot
        fields = '__all__'
