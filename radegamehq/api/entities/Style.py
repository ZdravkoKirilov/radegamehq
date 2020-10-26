from django.db import models

from ..mixins.EntityBase import EntityBase, WithModule


class Style(EntityBase, WithModule):
    rotation = models.IntegerField(null=True, blank=True)
    border_radius = models.IntegerField(null=True, blank=True)
    opacity = models.IntegerField(null=True, blank=True)
    skew = models.IntegerField(null=True, blank=True)
    scale = models.IntegerField(null=True, blank=True)

    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    y = models.IntegerField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    z = models.IntegerField(null=True, blank=True)

    stroke_color = models.TextField(null=True, blank=True)
    stroke_thickness = models.IntegerField(null=True, blank=True)
    fill = models.TextField(null=True, blank=True)
    tint = models.TextField(null=True, blank=True)

    font_size = models.IntegerField(null=True, blank=True)
    font_family = models.TextField(null=True, blank=True)
    font_style = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
