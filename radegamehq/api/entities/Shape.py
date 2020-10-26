from django.db import models

from ..mixins.EntityBase import WithStyle, EntityBase, WithModule


class Shape(WithStyle, EntityBase, WithModule):
    type = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class ShapePoint(models.Model):
    owner = models.ForeignKey(
        Shape, blank=True, null=True, on_delete=models.CASCADE, related_name='points')

    x = models.IntegerField()
    y = models.IntegerField()
