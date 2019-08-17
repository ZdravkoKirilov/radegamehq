from rest_framework import serializers

from ..entities.Choice import ChoiceOption, Choice
from ..mixins.NestedSerializing import with_nesting


class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = '__all__'


@with_nesting([
    {'name': 'options', 'model': ChoiceOption, 'm2m': False, 'serializer': ChoiceOptionSerializer},
])
class ChoiceSerializer(serializers.ModelSerializer):
    options = ChoiceOptionSerializer(many=True)

    class Meta:
        model = Choice
        fields = '__all__'
