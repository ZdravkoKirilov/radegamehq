from django.db import models

from ..mixins.EntityBase import EntityBase, WithStakes


class Condition(EntityBase, WithStakes):
    clause = models.ForeignKey('Expression', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return "{}".format(self.name)
