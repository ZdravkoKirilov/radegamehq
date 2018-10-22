from django.db import models

from api.mixins.EntityBase import EntityBase

from .Stack import EffectStack
from .Pool import Pool


class Field(EntityBase):
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=255)

    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, null=True, blank=True)

    cost = models.ManyToManyField(EffectStack, related_name='field_cost')
    award = models.ManyToManyField(EffectStack, related_name='field_award')
    penalty = models.ManyToManyField(EffectStack, related_name='field_penalty')

    effect_pool = models.ManyToManyField(Pool, related_name='field_effect_pool')

    def __str__(self):
        return "{}".format(self.name)
