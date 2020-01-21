from django.db import models

from ..mixins.EntityBase import EntityBase


class Style(EntityBase, models.Model):
    rotation = models.TextField(null=True, blank=True)
    border_radius = models.TextField(null=True, blank=True)
    opacity = models.TextField(null=True, blank=True)
    skew = models.TextField(null=True, blank=True)

    width = models.TextField(null=True, blank=True)
    height = models.TextField(null=True, blank=True)

    y = models.TextField(null=True, blank=True)
    x = models.TextField(null=True, blank=True)

    stroke_color = models.TextField(null=True, blank=True)
    stroke_thickness = models.TextField(null=True, blank=True)
    fill = models.TextField(null=True, blank=True)

    font_size = models.TextField(null=True, blank=True)
    font_family = models.TextField(null=True, blank=True)
    font_style = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
