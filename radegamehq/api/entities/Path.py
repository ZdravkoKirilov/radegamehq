from django.db import models

from .Game import Game
from .Slot import Slot


class Path(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)

    from_slot = models.ForeignKey(
        Slot,
        related_name='path_from_loc',
        on_delete=models.CASCADE,
    )
    to_slot = models.ForeignKey(
        Slot,
        related_name='path_to_loc',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format('From: ' + self.from_slot.name + ' To: ' + self.to_slot.name)
