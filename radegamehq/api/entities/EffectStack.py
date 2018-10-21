from django.db import models

from api.mixins.EntityBase import EntityBase

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT')
)


class EffectStack(EntityBase):
    image = models.ImageField(upload_to='stack_images', null=True, blank=True, max_length=None)

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])
