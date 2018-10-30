from django.db import models

from api.mixins.EntityBase import EntityBase
from .Stack import Stack

CHOICE_MODES = (
    ('TRAP', 'TRAP'),
    ('TRIGGER', 'TRIGGER'),
    ('HYBRID', 'HYBRID'),  # both trap and trigger
    ('AUTO', 'AUTO')  # for internal, 'hidden' logic
)


class Choice(EntityBase):
    image = models.ImageField(upload_to='choice_images', blank=True, null=True, max_length=None)

    cost = models.ManyToManyField(Stack, related_name='choice_cost', blank=True)  # cost to play
    condition = models.ManyToManyField(Stack, related_name='choice_condition',
                                       blank=True)  # enables you to play it

    restricted = models.ManyToManyField(Stack, related_name='choice_restricted',
                                        blank=True)  # who cant have it in hand: IS_FACTION, others implicitly can
    allowed = models.ManyToManyField(Stack, related_name='choice_allowed',
                                     blank=True)  # who can have it in hand: IS_FACTION, others implicitly cant

    mode = models.CharField(choices=CHOICE_MODES, default=CHOICE_MODES[0][1], max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class ChoiceOption(models.Model):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='options', null=True, blank=True)

    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to='choice_option_images', blank=True, null=True, max_length=None)

    effect = models.ManyToManyField(Stack)

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
