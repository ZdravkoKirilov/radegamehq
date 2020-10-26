from django.db import models

from ..mixins.EntityBase import EntityBase, WithVersion


class Module(EntityBase, WithVersion):

    loader = models.ForeignKey(
        'Widget', null=True, blank=True, on_delete=models.SET_NULL, related_name='loader')
    entry = models.ForeignKey('Widget', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='entry%(class)ss')

    dependencies = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
