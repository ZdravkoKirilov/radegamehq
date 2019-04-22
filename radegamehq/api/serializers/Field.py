from rest_framework import serializers

from ..entities.Field import Field
from ..entities.Group import Group

from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'cost', 'model': Group, 'm2m': True},
    {'name': 'risk', 'model': Group, 'm2m': True},
    {'name': 'done', 'model': Group, 'm2m': True},
    {'name': 'undone', 'model': Group, 'm2m': True},
])
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
