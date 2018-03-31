import copy

from rest_framework import serializers

from api.entities.Resource import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'description', 'image', 'game')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        data_copy = copy.deepcopy(data)
        if 'image' in data_copy and type(data_copy['image']) is str:
            data_copy.pop('image')
        value = super(ResourceSerializer, self).to_internal_value(data_copy)
        return value