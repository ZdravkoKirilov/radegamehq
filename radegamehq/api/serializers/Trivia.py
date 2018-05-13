from django.db import transaction
from rest_framework import serializers
from typing import Dict

from ..entities.Trivia import TriviaAnswerEffect, TriviaAnswer, Trivia

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField


class TriviaAnswerEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaAnswerEffect
        fields = ('id', 'activity')


class TriviaAnswerSerializer(serializers.ModelSerializer):
    effect = TriviaAnswerEffectSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)
    id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = TriviaAnswer
        fields = ('id', 'description', 'image', 'effect')


class TriviaSerializer(serializers.ModelSerializer):
    answers = TriviaAnswerSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Trivia
        fields = ('id', 'name', 'description', 'image', 'game', 'answers')
        read_only_fields = ('date_created', 'date_modified')

    def to_internal_value(self, data):
        sanitize_image(data)
        for item in data['answers']:
            sanitize_image(item)
        value = super(TriviaSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        answers = validated_data.pop('answers')

        instance = Trivia.objects.create(name=validated_data['name'],
                                         description=validated_data['description'],
                                         game=validated_data['game'], )

        if 'image' in validated_data:
            instance.image = validated_data['image']

        instance.save()

        for item in answers:
            self.save_trivia_answer(item, instance)

        return instance

    def update(self, instance: Trivia, validated_data):
        answers = validated_data.pop('answers')
        existing_answers = TriviaAnswer.objects.filter(trivia=instance)
        existing_answer_ids = [item['id'] for item in answers if 'id' in item]

        try:
            existing_answers.exclude(pk__in=existing_answer_ids).delete()
        except TriviaAnswer.DoesNotExist:
            pass

        for item in answers:
            try:
                obj = TriviaAnswer.objects.get(pk=item['id'])
                self.save_trivia_answer(item, instance, obj)
            except (TriviaAnswer.DoesNotExist, KeyError) as e:
                self.save_trivia_answer(item, instance)

        if 'image' in validated_data:
            instance.image = validated_data.pop('image')

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    @classmethod
    def save_trivia_answer(cls, item: Dict[str, any], owner: Trivia, obj=None):

        if obj is None:
            obj = TriviaAnswer(trivia=owner, description=item['description'])

        obj.__dict__.update(**item)
        obj.save()

        effects = item.pop('effect')
        effect_ids = [item['activity'].id for item in effects]
        existing_effects = TriviaAnswerEffect.objects.filter(answer=obj)

        try:
            existing_effects.exclude(activity__in=effect_ids).delete()
        except TriviaAnswerEffect.DoesNotExist:
            pass

        for item in effects:
            try:
                TriviaAnswerEffect.objects.get(answer=obj, activity=item['activity'])
            except TriviaAnswerEffect.DoesNotExist:
                cls.save_answer_effect(item, obj)

        return obj

    @classmethod
    def save_answer_effect(cls, item: Dict[str, any], owner: TriviaAnswer):
        obj = TriviaAnswerEffect(answer=owner, activity=item['activity'])
        obj.save()
