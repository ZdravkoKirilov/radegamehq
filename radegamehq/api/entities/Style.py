from django.db import models

from ..mixins.EntityBase import EntityBase


class Style(EntityBase, models.Model):
    frame = models.IntegerField(null=True, blank=True)
    rotation = models.TextField(null=True, blank=True)

    width = models.TextField(null=True, blank=True)
    height = models.TextField(null=True, blank=True)
    stroke_color = models.TextField(null=True, blank=True)
    stroke_thickness = models.TextField(null=True, blank=True)
    opacity = models.TextField(null=True, blank=True)

    hidden = models.NullBooleanField(blank=True, default=False)

    def __str__(self):
        return "{}".format(self.name)
