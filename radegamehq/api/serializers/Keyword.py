from rest_framework import serializers

from ..entities.Keyword import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
