from rest_framework import serializers

from ..entities.Group import GroupItem, Group
from ..entities.Keyword import Keyword
from ..entities.Condition import Condition
from ..entities.Game import Setup

from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'cost', 'model': Group, 'm2m': True},
    {'name': 'enable', 'model': Condition, 'm2m': True},
    {'name': 'disable', 'model': Condition, 'm2m': True},
    {'name': 'setups', 'model': Setup, 'm2m': True},
])
class GroupItemSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = GroupItem
        fields = '__all__'


@with_nesting([
    {'name': 'items', 'model': GroupItem, 'm2m': False, 'serializer': GroupItemSerializer},
    {'name': 'keywords', 'model': Keyword, 'm2m': True}
])
class GroupSerializer(serializers.ModelSerializer):
    items = GroupItemSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
