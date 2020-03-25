from rest_framework import serializers

from ..entities.Transition import Transition
from ..mixins.NestedSerializing import with_nesting
from ..entities.Stage import Stage, Slot, SlotHandler, StageFrame


class SlotHandlerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlotHandler
        exclude = ('owner',)


class StageFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageFrame
        fields = '__all__'


@with_nesting([
    {'name': 'handlers', 'model': SlotHandler, 'm2m': False, 'serializer': SlotHandlerSerializer},
    {'name': 'transitions', 'model': Transition, 'm2m': True},
])
class SlotSerializer(serializers.ModelSerializer):
    handlers = SlotHandlerSerializer(many=True, allow_null=True)
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Slot
        fields = '__all__'


@with_nesting([
    {'name': 'slots', 'model': Slot, 'm2m': False, 'serializer': SlotSerializer},
    {'name': 'frames', 'model': StageFrame, 'm2m': False, 'serializer': StageFrameSerializer},
])
class StageSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True)
    frames = StageFrameSerializer(many=True)

    class Meta:
        model = Stage
        fields = '__all__'
