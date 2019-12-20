from django.db import models

from ..mixins.EntityBase import EntityBase, WithTemplate


class Action(EntityBase, WithTemplate):

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, blank=True, null=True, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False)

    payload = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
