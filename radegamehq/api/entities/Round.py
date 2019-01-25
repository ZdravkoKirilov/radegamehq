from django.db import models

from api.mixins.EntityBase import EntityBase, WithBoard, WithCondition, WithStakes


class Round(EntityBase, WithBoard, WithCondition, WithStakes):

    replay_count = models.IntegerField(null=True, blank=True)  # how many tries to pass the condition
    repeat = models.IntegerField(null=True, blank=True)  # repeat X times before going to the next round

    phases = models.ManyToManyField('Phase', related_name='round_phases')
    phase_order = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
