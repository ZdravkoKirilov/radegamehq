from django.db import models

from api.mixins.EntityBase import EntityBase

from .EffectGroup import EffectGroup
from .EffectStack import EffectStack


class Round(EntityBase):
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, blank=True, null=True, related_name="round_stage")

    image = models.ImageField(upload_to='round_images', blank=True, null=True, max_length=255)

    replay_count = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    condition = models.ManyToManyField(EffectStack, related_name='round_condition')
    penalty = models.ManyToManyField(EffectStack, related_name='round_penalty')
    award = models.ManyToManyField(EffectStack, related_name='round_award')

    effect_pool = models.ManyToManyField(EffectGroup, related_name='round_effect_pool')

    def __str__(self):
        return "{}".format(self.name)
