from django.db import models
from ..mixins.EntityBase import EntityBase


class Transition(EntityBase):
    trigger = models.TextField()

    animation = models.ForeignKey('Animation', on_delete=models.SET_NULL, related_name='animation', blank=True,
                                  null=True)
    sound = models.TextField(null=True, blank=True)

    enabled = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
