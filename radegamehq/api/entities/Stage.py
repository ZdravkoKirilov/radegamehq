from django.db import models

from ..mixins.EntityBase import EntityBase, WithImage


class Stage(EntityBase, WithImage):
    width = models.IntegerField()
    height = models.IntegerField()

    get_slots = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
