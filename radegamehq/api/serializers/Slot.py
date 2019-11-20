from rest_framework import serializers

from ..entities.Slot import Slot, SlotHandler, SlotFrame
from ..entities.Transition import Transition
from ..mixins.NestedSerializing import with_nesting


class SlotHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotHandler
        fields = '__all__'


class SlotFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotFrame
        fields = '__all__'


@with_nesting([
    {'name': 'handlers', 'model': SlotHandler, 'm2m': False, 'serializer': SlotHandlerSerializer},
    {'name': 'transitions', 'model': Transition, 'm2m': True},
    {'name': 'frames', 'model': SlotFrame, 'm2m': False, 'serializer': SlotFrameSerializer},
])
class SlotSerializer(serializers.ModelSerializer):
    handlers = SlotHandlerSerializer(many=True)
    frames = SlotFrameSerializer(many=True)

    class Meta:
        model = Slot
        fields = '__all__'
