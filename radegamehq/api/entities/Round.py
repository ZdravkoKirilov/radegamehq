from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard


class Round(EntityBase, WithBoard):
    preload = models.TextField(null=True, blank=True)
    load_done = models.TextField(null=True, blank=True)

    loader = models.ForeignKey('Stage', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.name)


class Phase(models.Model):
    owner = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='phases', blank=True, null=True)
    phase = models.ForeignKey('Phase', on_delete=models.CASCADE, related_name="phase_slot")
