from rest_framework import serializers

from ..entities.Transition import Transition
from ..mixins.NestedSerializing import with_nesting
from ..entities.Widget import Widget, WidgetNode, NodeHandler, WidgetFrame, NodeLifecycle


class NodeHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeHandler
        exclude = ('owner',)


class NodeLifecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeLifecycle
        exclude = ('owner',)


class WidgetFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetFrame
        fields = '__all__'


@with_nesting([
    {'name': 'handlers', 'model': NodeHandler, 'm2m': False, 'serializer': NodeHandlerSerializer},
    {'name': 'lifecycles', 'model': NodeLifecycle, 'm2m': False, 'serializer': NodeLifecycleSerializer},
    {'name': 'transitions', 'model': Transition, 'm2m': True},
])
class NodeSerializer(serializers.ModelSerializer):
    handlers = NodeHandlerSerializer(many=True, allow_null=True)
    lifecycles = NodeLifecycleSerializer(many=True, allow_null=True)
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = WidgetNode
        fields = '__all__'


@with_nesting([
    {'name': 'frames', 'model': WidgetFrame, 'm2m': False, 'serializer': WidgetFrameSerializer},
])
class WidgetSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True)
    frames = WidgetFrameSerializer(many=True)

    class Meta:
        model = Widget
        fields = '__all__'
