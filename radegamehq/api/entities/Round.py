from django.db import models

from api.entities.Game import Game


class Round(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.OneToOneField('Stage', on_delete=models.SET_NULL, blank=True, null=True, related_name="round_stage")
    image = models.FileField(upload_to='round_images', blank=True, null=True, max_length=200)
    replay = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class RoundQuest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_quest')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.quest.name)


class RoundCondition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_condition')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.quest.name)


class RoundActivity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_activity')
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.activity.name)

    class Meta:
        verbose_name_plural = 'Round activities'