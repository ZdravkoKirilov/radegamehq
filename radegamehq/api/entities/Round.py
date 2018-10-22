from django.db import models

from api.mixins.EntityBase import EntityBase

from .Pool import Pool
from .Stack import EffectStack


class Round(EntityBase):
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, blank=True, null=True, related_name="round_stage")

    image = models.ImageField(upload_to='round_images', blank=True, null=True, max_length=None)

    replay_count = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    condition = models.ManyToManyField(EffectStack, related_name='round_condition')
    penalty = models.ManyToManyField(EffectStack, related_name='round_penalty')
    award = models.ManyToManyField(EffectStack, related_name='round_award')

    effect_pool = models.ManyToManyField(Pool, related_name='round_effect_pool')

    def __str__(self):
        return "{}".format(self.name)


class Phase(models.Model):

    owner = models.ForeignKey(Round, on_delete=models.CASCADE, null=True, blank=True)

    image = models.ImageField(upload_to='phase_images', blank=True, null=True, max_length=None)
    name = models.CharField(max_length=255)
