from rest_framework import serializers

from ..entities.Handler import Handler


class HandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handler
        fields = '__all__'
