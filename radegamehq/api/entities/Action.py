from django.db import models

from ..mixins.EntityBase import EntityBase


class Action(EntityBase):

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, blank=True, null=True, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False)

    target = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='action_target')

    subject = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='action_subject')

    value = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='action_value')

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
