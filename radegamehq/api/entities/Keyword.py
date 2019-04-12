from django.db import models

from ..mixins.EntityBase import EntityBase


class Keyword(EntityBase, models.Model):

    def __str__(self):
        return "{}".format(self.name)
