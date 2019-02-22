from rest_framework import serializers


class SetField(serializers.ListField):
    def to_representation(self, value):
        data = super().to_representation(value)
        return set(data)

    def to_internal_value(self, data):
        return set(data)
