from django.db import models

from api.entities.Field import BoardField
from api.entities.Game import Game


class MapLocation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    width = models.FloatField()
    height = models.FloatField()
    left = models.FloatField()
    top = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)
    field = models.OneToOneField(
        BoardField,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.field.name)