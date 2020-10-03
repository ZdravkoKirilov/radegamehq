from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard


class Module(EntityBase, WithBoard):
    preload = models.TextField(null=True, blank=True)
    load_done = models.TextField(null=True, blank=True)

    loader = models.ForeignKey('Widget', null=True, blank=True, on_delete=models.SET_NULL, related_name='loader')

    def __str__(self):
        return "{}".format(self.name)
