from django.db import models

from api.mixins.EntityBase import EntityBase

from .Stack import Stack
from .Pool import Pool


class Field(EntityBase):
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=255)

    cost = models.ManyToManyField(Stack, related_name='field_cost', blank=True)
    award = models.ManyToManyField(Stack, related_name='field_award', blank=True)
    penalty = models.ManyToManyField(Stack, related_name='field_penalty', blank=True)

    effect_pool = models.ManyToManyField(Pool, related_name='field_effect_pool', blank=True)

    def __str__(self):
        return "{}".format(self.name)
