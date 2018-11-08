from django.db import models

from api.entities.Game import Game
from api.entities.Location import Location


class Path(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)

    from_loc = models.ForeignKey(
        Location,
        related_name='path_from_loc',
        on_delete=models.CASCADE,
    )
    to_loc = models.ForeignKey(
        Location,
        related_name='path_to_loc',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format('From: ' + self.from_loc.name + ' To: ' + self.to_loc.name)
