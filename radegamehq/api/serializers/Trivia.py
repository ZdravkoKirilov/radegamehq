import copy

from django.db import transaction
from rest_framework import serializers

from api.entities.Activity import Activity
from api.entities.Trivia import TriviaAnswerEffect, TriviaAnswer, Trivia


class TriviaAnswerEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaAnswerEffect
        fields = ('id', 'activity')
        read_only_fields = ('date_created', 'date_modified')


class TriviaAnswerSerializer(serializers.ModelSerializer):
    effect = TriviaAnswerEffectSerializer(many=True, source='trivia_answer_effect')

    class Meta:
        model = TriviaAnswer
        fields = ('id', 'description', 'image', 'effect')
        read_only_fields = ('date_created', 'date_modified')


class TriviaSerializer(serializers.ModelSerializer):
    answers = TriviaAnswerSerializer(many=True, source='trivia_answer')

    class Meta:
        model = Trivia
        fields = ('id', 'name', 'description', 'image', 'game', 'answers')
        read_only_fields = ('date_created', 'date_modified')

    def serialize_answers(self, data, nested_prop):
        result = dict()
        new_data = copy.deepcopy(data)

        for key, value in data.items():
            if nested_prop in key:
                index = key[len(nested_prop) + 1]
                new_key = key[len(nested_prop) + 3:]

                if index not in result:
                    result[index] = dict()

                result[index][new_key] = value
                del new_data[key]

        new_data[nested_prop] = result
        return new_data

    def serialize_effect(self, data, nested_prop):
        new_data = copy.deepcopy(data)

        for key, value in data.items():
            new_item = new_data[key]
            for key2, value2 in value.items():
                if nested_prop in key2:
                    if nested_prop not in new_item:
                        new_item[nested_prop] = list()

                    new_item[nested_prop].append(value2)
                else:
                    new_key = key2[1:len(key2) - 1]
                    new_item[new_key] = value2
                del new_item[key2]

        return new_data

    def to_internal_value(self, data):
        without_effect = self.serialize_answers(data, 'answers')
        answers = self.serialize_effect(without_effect['answers'], 'effect')

        value = super(TriviaSerializer, self).to_internal_value(data)
        value['answers'] = [answers[key] for key in answers]
        return value

    @transaction.atomic
    def create(self, validated_data):
        answers = validated_data.pop('answers')
        instance = Trivia.objects.create(name=validated_data['name'],
                                         description=validated_data['description'],
                                         mode=validated_data['mode'],
                                         game=validated_data['game'], )

        if 'image' in validated_data and type(validated_data['image']) is not str:
            instance.image = validated_data['image']

        for item in answers:
            answer = TriviaAnswer.objects.create(trivia=instance, description=item['description'])
            if 'image' in item and type(item['image']) is not str:
                answer.image = item['image']
            answer.save()
            try:
                self.create_answer_effect(item['effect'], answer)
            except KeyError:
                pass

        instance.save()
        return instance

    def update(self, instance, validated_data):
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
                obj.description = item['description']
            except (TriviaAnswer.DoesNotExist, KeyError) as e:
                obj = TriviaAnswer.objects.create(trivia=instance, description=item['description'])
            finally:
                if 'image' in item and type(item['image']) is not str:
                    obj.image = item['image']
                obj.save()
                try:
                    self.update_answer_effect(item['effect'], obj)
                except KeyError:
                    self.update_answer_effect([], obj)

        if 'name' in validated_data:
            instance.name = validated_data.pop('name')
        if 'description' in validated_data:
            instance.description = validated_data.pop('description')
        if 'image' in validated_data and type(validated_data['image']) is not str:
            instance.image = validated_data.pop('image')
        if 'mode' in validated_data:
            instance.mode = validated_data.pop('mode')

        instance.save()
        return instance

    def update_answer_effect(self, data, answer):
        existing_effects = TriviaAnswerEffect.objects.filter(answer=answer)
        existing_effect_ids = [item for item in data]

        try:
            existing_effects.exclude(activity__in=existing_effect_ids).delete()
        except TriviaAnswerEffect.DoesNotExist:
            pass

        for item in data:
            activity = Activity.objects.get(pk=item)
            try:
                TriviaAnswerEffect.objects.get(activity=activity, answer=answer)
            except TriviaAnswerEffect.DoesNotExist:
                TriviaAnswerEffect.objects.create(activity=activity, answer=answer)

    def create_answer_effect(self, data, answer):
        for item in data:
            activity = Activity.objects.get(pk=item)
            TriviaAnswerEffect.objects.create(activity=activity, answer=answer)