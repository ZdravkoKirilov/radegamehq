from django.db import models

from ..mixins.EntityBase import EntityBase


class State(EntityBase, models.Model):
    display_name = models.TextField(null=True, blank=True)

    style = models.ForeignKey('Style', on_delete=models.SET_NULL, null=True, blank=True)
    sound = models.ForeignKey('Sound', on_delete=models.SET_NULL, null=True, blank=True)
    animation = models.ForeignKey('Animation', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
