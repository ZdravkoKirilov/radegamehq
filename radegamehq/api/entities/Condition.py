from django.db import models

from ..mixins.EntityBase import EntityBase, WithFrame, WithTemplate


class Condition(EntityBase, WithTemplate):
    clause = models.TextField(blank=True, null=True)
    passes = models.TextField(blank=True, null=True)
    fails = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return "{}".format(self.name)


class ConditionFrame(WithFrame):
    owner = models.ForeignKey(Condition, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
