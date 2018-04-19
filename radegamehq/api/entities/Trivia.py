from django.db import models

from api.entities.Activity import Activity
from api.entities.Game import Game


class Trivia(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='trivia_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class TriviaAnswer(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='trivia_answer')
    description = models.TextField(blank=False)
    image = models.FileField(upload_to='trivia_answer_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "Answer_{}_{}".format(self.id, self.trivia.name)


class TriviaAnswerEffect(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(TriviaAnswer, on_delete=models.CASCADE, related_name='trivia_answer_effect')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}_{}".format(self.answer.id, self.activity.name, self.id)