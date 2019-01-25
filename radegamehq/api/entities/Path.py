from django.db import models

from .Slot import Slot

from ..mixins.EntityBase import EntityBase, WithPermissions, WithRisk, WithStakes, WithBoard, WithCost


class Path(EntityBase, WithPermissions, WithRisk, WithStakes, WithBoard, WithCost):

    owner = models.ForeignKey('Stage', on_delete=models.CASCADE, related_name='path_owner')

    from_slot = models.ForeignKey(
        Slot,
        related_name='from_slot',
        on_delete=models.CASCADE,
    )
    to_slot = models.ForeignKey(
        Slot,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format('From: ' + self.from_slot.name + ' To: ' + self.to_slot.name)
