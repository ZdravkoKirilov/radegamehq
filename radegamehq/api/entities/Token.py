from django.db import models
from api.mixins.EntityBase import EntityBase


class Token(EntityBase):
    image = models.ImageField(upload_to='token_images', blank=True, null=True, max_length=None)

    start = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True)

    effect_pool = models.ManyToManyField('Pool', related_name='token_effect_pool', blank=True)

    restricted = models.ManyToManyField('Stack', related_name='token_restricted', blank=True)
    allowed = models.ManyToManyField('Stack', related_name='token_allowed', blank=True)

    def __str__(self):
        return self.name
