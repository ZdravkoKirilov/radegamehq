from django.db import models

from api.mixins.EntityBase import EntityBase

from .Pool import Pool
from .Stack import Stack


class Round(EntityBase):
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, blank=True, null=True, related_name="round_stage")

    image = models.ImageField(upload_to='round_images', blank=True, null=True, max_length=None)

    replay_count = models.IntegerField(null=True, blank=True)  # how many tries to pass the condition
    repeat = models.IntegerField(null=True, blank=True)  # repeat X times before going to the next round

    phases = models.ManyToManyField('Phase', related_name='round_phases')
    phase_order = models.TextField(null=True, blank=True)

    condition = models.ManyToManyField('Condition', related_name='round_condition')

    penalty = models.ManyToManyField(Stack, related_name='round_penalty')
    award = models.ManyToManyField(Stack, related_name='round_award')

    income = models.ManyToManyField(Stack, related_name='round_income')

    effect_pool = models.ManyToManyField(Pool, related_name='round_effect_pool')

    def __str__(self):
        return "{}".format(self.name)
