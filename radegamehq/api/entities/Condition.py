from django.db import models

from .Action import Action
from .Field import Field
from .Stack import EffectStack
from .Resource import Resource

from api.mixins.EntityBase import EntityBase

CLAIM = 'CLAIM'  # field, keyword
REACH = 'REACH'  # field, keyword
MEET = 'MEET'  # faction, keyword
AVOID = 'AVOID'  # faction, action, keyword
COMPLETE = 'COMPLETE'  # condition, keyword
TRIGGER = 'TRIGGER'  # condition, action, keyword
GATHER = 'GATHER'  # resource, keyword

# ROUND_IS
# ROUND_IS_AFTER
# ROUND_IS_BEFORE
# TAG_ROUND_IS
# TAG_ROUND_IS_NOT
# HAVE (resource, condition etc)
# HAVE_MAX
# PLAY_MAX
# IS_FACTION
# IS_TOKEN
# IS_KEYWORD

TYPE_CHOICES = (
    (CLAIM, CLAIM),
    (REACH, REACH),
    (MEET, MEET),
    (AVOID, AVOID),
    (COMPLETE, COMPLETE),
    (TRIGGER, TRIGGER),
    (GATHER, GATHER)
)

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT')
)


class Condition(EntityBase):
    image = models.ImageField(upload_to='condition_images', blank=True, null=True, max_length=255)

    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True, blank=True, related_name="condition_stage")

    award = models.ManyToManyField(EffectStack, related_name='condition_award')
    penalty = models.ManyToManyField(EffectStack, related_name='condition_penalty')

    restriction = models.ManyToManyField(EffectStack, related_name='condition_restriction')
    trap_mode = models.BooleanField(null=True, default=False)

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

    amount = models.IntegerField(blank=True, null=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)

# Do something at X round => can be done by composing 2 clauses: 1) the doing and 2) the circumstance
