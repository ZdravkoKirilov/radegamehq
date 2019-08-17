from rest_framework import serializers

from ..entities.Condition import Condition


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'
