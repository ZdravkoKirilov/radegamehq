from rest_framework import serializers

from ..entities.Expression import Expression


class ExpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expression
        fields = '__all__'
