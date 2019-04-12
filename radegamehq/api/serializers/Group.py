from rest_framework import serializers

from ..entities.Group import GroupItem, Group

from ..mixins.NestedSerializing import with_nesting


class GroupItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True)

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
