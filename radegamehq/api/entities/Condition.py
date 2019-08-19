from django.db import models

from ..mixins.EntityBase import EntityBase, WithStakes, WithFrame


class Condition(EntityBase, WithStakes):
    clause = models.ForeignKey('Expression', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return "{}".format(self.name)


class ConditionFrame(WithFrame):
    owner = models.ForeignKey(Condition, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
