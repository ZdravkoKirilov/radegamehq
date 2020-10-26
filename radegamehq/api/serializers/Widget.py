from rest_framework import serializers
from mypy_extensions import TypedDict

from ..mixins.NestedSerializing import with_nesting
from ..entities.Widget import Widget, WidgetNode, NodeHandler, NodeLifecycle


class NodeHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeHandler
        exclude = ('owner',)


class NodeLifecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeLifecycle
        exclude = ('owner',)


@with_nesting([
    {'name': 'handlers', 'model': NodeHandler,
        'm2m': False, 'serializer': NodeHandlerSerializer},
    {'name': 'lifecycles', 'model': NodeLifecycle,
        'm2m': False, 'serializer': NodeLifecycleSerializer},
])
class NodeSerializer(serializers.ModelSerializer):
    handlers = NodeHandlerSerializer(many=True, allow_null=True)
    lifecycles = NodeLifecycleSerializer(many=True, allow_null=True)

    class Meta:
        model = WidgetNode
        fields = '__all__'


@with_nesting([
    {'name': 'nodes', 'model': WidgetNode, 'm2m': False,
     'serializer': NodeSerializer},
])
class WidgetSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, allow_null=True,
                           allow_empty=True, default=[])

    class Meta:
        model = Widget
        fields = '__all__'
