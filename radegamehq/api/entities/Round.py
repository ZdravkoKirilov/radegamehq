from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard


class Round(EntityBase, WithBoard):
    preload = models.TextField(null=True, blank=True)
    load_done = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class PhaseSlot(models.Model):
    owner = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='phases', blank=True, null=True)
    phase = models.ForeignKey('Phase', on_delete=models.CASCADE)
