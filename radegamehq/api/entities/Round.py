from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithDone, WithDisplayName


class Round(EntityBase, WithBoard, WithDone, WithDisplayName):

    def __str__(self):
        return "{}".format(self.name)


class PhaseSlot(models.Model):
    owner = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='phases', blank=True, null=True)
    phase = models.ForeignKey('Phase', on_delete=models.CASCADE)
