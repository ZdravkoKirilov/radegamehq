from django.db import models

from api.entities.Activity import Activity
from api.entities.Field import BoardField
from api.entities.Game import Game
from api.entities.Resource import Resource
from api.entities.Round import Round


class Quest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.OneToOneField('Stage', on_delete=models.SET_NULL, null=True, blank=True, related_name="quest_stage")
    image = models.FileField(upload_to='quest_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class QuestCost(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_cost')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_cost_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cost_{}_{}".format(self.quest.name, self.activity.name)


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
    CLAIM_FIELD = 'CLAIM_FIELD'
    CLAIM_ANY_FIELDS = 'CLAIM_ANY_FIELDS'
    DEFEND_FIELD = 'DEFEND_FIELD'
    DEFEND_ANY_FIELDS = 'DEFEND_ANY_FIELDS'
    CLAIM_RESOURCE = 'CLAIM_RESOURCE'
    CLAIM_ANY_RESOURCE = 'CLAIM_ANY_RESOURCE'
    STEAL_ACTIVITY = 'STEAL_ACTIVITY'
    STEAL_ANY_ACTIVITY = 'STEAL_ANY_ACTIVITY'
    DISCARD_ACTIVITY = 'DISCARD_ACTIVITY'
    DISCARD_ANY_ACTIVITY = 'DISCARD_ANY_ACTIVITY'
    PLAY_ACTIVITY = 'PLAY_ACTIVITY'
    PLAY_ANY_ACTIVITY = 'PLAY_ANY_ACTIVITY'

    TYPE_CHOICES = (
        (CLAIM_FIELD, 'CLAIM_FIELD'),
        (CLAIM_ANY_FIELDS, 'CLAIM_ANY_FIELDS'),
        (DEFEND_FIELD, 'DEFEND_FIELD'),
        (DEFEND_ANY_FIELDS, 'DEFEND_ANY_FIELDS'),
        (CLAIM_RESOURCE, 'CLAIM_RESOURCE'),
        (CLAIM_ANY_RESOURCE, 'CLAIM_ANY_RESOURCE'),
        (STEAL_ACTIVITY, 'STEAL_ACTIVITY'),
        (STEAL_ANY_ACTIVITY, 'STEAL_ANY_ACTIVITY'),
        (DISCARD_ACTIVITY, 'DISCARD_ACTIVITY'),
        (DISCARD_ANY_ACTIVITY, 'DISCARD_ANY_ACTIVITY'),
        (PLAY_ACTIVITY, 'PLAY_ACTIVITY'),
        (PLAY_ANY_ACTIVITY, 'PLAY_ANY_ACTIVITY'),
    )

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition_quest', blank=True,
                              null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_condition_activity',
                                 blank=True,
                                 null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_cond_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_cond_field', blank=True,
                              null=True)
    byRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_byRound',
                                on_delete=models.SET_NULL)
    atRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_atRound',
                                on_delete=models.SET_NULL)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)