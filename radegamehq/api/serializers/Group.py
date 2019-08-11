from rest_framework import serializers

from ..entities.Group import GroupItem, Group
from ..entities.Condition import Condition
from ..entities.Setup import Setup

from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'cost', 'model': Group, 'm2m': True},
    {'name': 'enable', 'model': Condition, 'm2m': True},
    {'name': 'disable', 'model': Condition, 'm2m': True},
    {'name': 'setups', 'model': Setup, 'm2m': True},
])
class GroupItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupItem
        fields = '__all__'


@with_nesting([
    {'name': 'items', 'model': GroupItem, 'm2m': False, 'serializer': GroupItemSerializer},
])
class GroupSerializer(serializers.ModelSerializer):
    items = GroupItemSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
