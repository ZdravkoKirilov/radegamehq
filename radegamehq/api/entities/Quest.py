from django.db import models

from .Activity import Activity
from .Field import Field
from .Game import Game
from .Resource import Resource
from .Round import Round

CLAIM = 'CLAIM'  # field, keyword
REACH = 'REACH'  # field, ketword
MEET = 'MEET'  # faction, keyword
AVOID = 'AVOID'  # faction, activity, keyword
COMPLETE = 'COMPLETE'  # quest, keyword
TRIGGER = 'TRIGGER'  # quest, activity, keyword

TYPE_CHOICES = (
    (CLAIM, CLAIM),
    (REACH, REACH),
    (MEET, MEET),
    (AVOID, AVOID),
    (COMPLETE, COMPLETE),
    (TRIGGER, TRIGGER),
)


class Quest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='quest_images', blank=True, null=True, max_length=255)
    keywords = models.CharField(null=True, blank=True, max_length=255)

    stage = models.OneToOneField('Stage', on_delete=models.SET_NULL, null=True, blank=True, related_name="quest_stage")

    def __str__(self) -> str:
        return "{}".format(self.name)


class QuestAward(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_award')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_award_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Award_{}_{}".format(self.quest.name, self.activity.name)


class QuestPenalty(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_penalty')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_pen_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Penalty_{}_{}".format(self.quest.name, self.activity.name)

    class Meta:
        verbose_name_plural = 'Quest penalties'


class QuestCondition(models.Model):
    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition_quest', blank=True,
                              null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_condition_activity',
                                 blank=True,
                                 null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_cond_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='quest_cond_field', blank=True,
                              null=True)
    keywords = models.CharField(null=True, blank=True, max_length=255)
    byRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_byRound',
                                on_delete=models.SET_NULL)
    atRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_atRound',
                                on_delete=models.SET_NULL)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)
