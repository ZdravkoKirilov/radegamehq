from django.db import transaction
from rest_framework import serializers
from typing import Dict

from ..entities.Choice import ChoiceOption, Choice

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField


class ChoiceOptionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = ChoiceOption
        fields = ('id', 'description', 'image', 'effect')


class ChoiceSerializer(serializers.ModelSerializer):
    options = ChoiceOptionSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Choice
        fields = ('id', 'name', 'description', 'image', 'game', 'options')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        sanitize_image(data)
        for item in data['options']:
            sanitize_image(item)
        value = super(ChoiceSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        options = validated_data.pop('options')

        instance = Choice.objects.create(name=validated_data['name'],
                                         description=validated_data['description'],
                                         game=validated_data['game'], )

        if 'image' in validated_data:
            instance.image = validated_data['image']

        instance.save()

        for item in options:
            self.save_choice_option(item, instance)

        return instance

    def update(self, instance: Choice, validated_data):
        # answers = validated_data.pop('answers')
        # existing_answers = ChoiceOption.objects.filter(trivia=instance)
        # existing_answer_ids = [item['id'] for item in answers if 'id' in item]
        #
        # try:
        #     existing_answers.exclude(pk__in=existing_answer_ids).delete()
        # except ChoiceOption.DoesNotExist:
        #     pass
        #
        # for item in answers:
        #     try:
        #         obj = ChoiceOption.objects.get(pk=item['id'])
        #         self.save_choice_option(item, instance, obj)
        #     except (ChoiceOption.DoesNotExist, KeyError) as e:
        #         self.save_choice_option(item, instance)

        if 'image' in validated_data:
            instance.image = validated_data.pop('image')

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_choice_option(cls, item: Dict[str, any], owner: Choice, obj=None):

        if obj is None:
            obj = ChoiceOption(trivia=owner, description=item['description'])

        obj.__dict__.update(**item)
        obj.save()

        # effects = item.pop('effect')
        # effect_ids = [item['activity'].id for item in effects]
        # existing_effects = TriviaAnswerEffect.objects.filter(answer=obj)
        #
        # try:
        #     existing_effects.exclude(activity__in=effect_ids).delete()
        # except TriviaAnswerEffect.DoesNotExist:
        #     pass
        #
        # for item in effects:
        #     try:
        #         TriviaAnswerEffect.objects.get(answer=obj, activity=item['activity'])
        #     except TriviaAnswerEffect.DoesNotExist:
        #         cls.save_answer_effect(item, obj)

        return obj

    # @classmethod
    # def save_answer_effect(cls, item: Dict[str, any], owner: ChoiceOption):
    #     obj = TriviaAnswerEffect(answer=owner, activity=item['activity'])
    #     obj.save()
