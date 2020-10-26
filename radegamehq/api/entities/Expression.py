from django.db import models
from ..mixins.EntityBase import EntityBase, WithModule


class Expression(EntityBase, WithModule):
    code = models.TextField(max_length=None)

    def __str__(self):
        return "{}".format(self.name)
