from django.db import models

from api.entities.Game import Game
from api.entities.Location import MapLocation


class MapPath(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    fromLoc = models.ForeignKey(
        MapLocation,
        related_name='from_loc+',
        on_delete=models.CASCADE,
    )
    toLoc = models.ForeignKey(
        MapLocation,
        related_name='to_loc+',
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return "{}".format('From: ' + self.fromLoc.field.name + ' To: ' + self.toLoc.field.name)
