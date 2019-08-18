from rest_framework import serializers

from ..entities.Choice import ChoiceOption, Choice, ChoiceTip, ChoiceFrame
from ..entities.Keyword import Keyword
from ..mixins.NestedSerializing import with_nesting


@with_nesting([
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class ChoiceTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceTip
        fields = '__all__'


@with_nesting([
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = '__all__'


class ChoiceFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceFrame
        fields = '__all__'


@with_nesting([
    {'name': 'options', 'model': ChoiceOption, 'm2m': False, 'serializer': ChoiceOptionSerializer},
    {'name': 'tips', 'model': ChoiceTip, 'm2m': False, 'serializer': ChoiceTipSerializer},
    {'name': 'frames', 'model': ChoiceFrame, 'm2m': False, 'serializer': ChoiceFrameSerializer},
    {'name': 'keywords', 'model': Keyword, 'm2m': True},
])
class ChoiceSerializer(serializers.ModelSerializer):
    options = ChoiceOptionSerializer(many=True)
    tips = ChoiceTipSerializer(many=True)
    frames = ChoiceFrameSerializer(many=True)

    class Meta:
        model = Choice
        fields = '__all__'
