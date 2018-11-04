from django.db import models

from ..entities.Field import Field
from ..entities.Game import Game


class Location(models.Model):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    width = models.FloatField()
    height = models.FloatField()

    x = models.FloatField()
    y = models.FloatField()

    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True, blank=True)
    token = models.ForeignKey('Token', on_delete=models.SET_NULL, null=True, blank=True)

    allowed = models.ManyToManyField('Stack', blank=True)

    def __str__(self):
        return "{}".format(self.field.name)
