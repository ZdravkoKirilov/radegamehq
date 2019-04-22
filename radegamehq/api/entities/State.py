from django.db import models

from ..mixins.EntityBase import EntityBase


class State(EntityBase, models.Model):
    display_name = models.TextField(null=True, blank=True)

    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)
    style = models.ForeignKey('Style', on_delete=models.CASCADE, null=True, blank=True)
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
