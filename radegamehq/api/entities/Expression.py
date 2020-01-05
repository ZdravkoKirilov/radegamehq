from django.db import models
from ..mixins.EntityBase import EntityBase


class Expression(EntityBase):
    preload_as = models.CharField(max_length=255, blank=True, null=True)
    code = models.TextField(max_length=None)

    def __str__(self):
        return "{}".format(self.name)
