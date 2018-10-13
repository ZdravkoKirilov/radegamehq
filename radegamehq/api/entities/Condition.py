from django.db import models

from .Action import Action
from .Field import Field
from .EffectStack import EffectStack
from .Resource import Resource
from .Round import Round

from api.mixins.EntityBase import EntityBase

CLAIM = 'CLAIM'  # field, keyword
REACH = 'REACH'  # field, keyword
MEET = 'MEET'  # faction, keyword
AVOID = 'AVOID'  # faction, action, keyword
COMPLETE = 'COMPLETE'  # condition, keyword
TRIGGER = 'TRIGGER'  # condition, action, keyword
GATHER = 'GATHER'  # resource, keyword

TYPE_CHOICES = (
    (CLAIM, CLAIM),
    (REACH, REACH),
    (MEET, MEET),
    (AVOID, AVOID),
    (COMPLETE, COMPLETE),
    (TRIGGER, TRIGGER),
    (GATHER, GATHER)
)


class Condition(models.Model, EntityBase):
    image = models.ImageField(upload_to='condition_images', blank=True, null=True, max_length=255)

    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True, blank=True, related_name="condition_stage")

    award = models.ManyToManyField(EffectStack, related_name='condition_award')
    penalty = models.ManyToManyField(EffectStack, related_name='condition_penalty')

    def __str__(self) -> str:
        return "{}".format(self.name)


class ConditionClause(models.Model):
    owner = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='condition_clause')

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='condition_clause_condition',
                                  blank=True,
                                  null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='condition_clause_action',
                               blank=True,
                               null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='condition_clause_resource',
                                 blank=True,
                                 null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='condition_clause_field', blank=True,
                              null=True)
    keyword = models.CharField(null=True, blank=True, max_length=255)

    by_round = models.ForeignKey(Round, blank=True, null=True, related_name='condition_clause_byround',
                                 on_delete=models.SET_NULL)
    at_round = models.ForeignKey(Round, blank=True, null=True, related_name='condition_clause_atround',
                                 on_delete=models.SET_NULL)

    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)
