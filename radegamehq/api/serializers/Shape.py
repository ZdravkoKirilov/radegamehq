from rest_framework import serializers

from ..entities.Shape import Shape, ShapePoint
from ..mixins.NestedSerializing import with_nesting


class ShapePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShapePoint
        fields = '__all__'


@with_nesting([
    {'name': 'points', 'model': ShapePoint, 'm2m': False, 'serializer': ShapePointSerializer},
])
class ShapeSerializer(serializers.ModelSerializer):
    steps = ShapePointSerializer(many=True)

    class Meta:
        model = Shape
        fields = '__all__'
