from django.db import models

from ..entities.Field import Field
from ..entities.Game import Game


class Location(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    width = models.FloatField()
    height = models.FloatField()

    x = models.FloatField()
    y = models.FloatField()

    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)
    field = models.OneToOneField(Field, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.field.name)
