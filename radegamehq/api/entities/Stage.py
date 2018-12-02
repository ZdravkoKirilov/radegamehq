from django.db import models

from ..mixins.EntityBase import EntityBase


class Stage(EntityBase, models.Model):
    image = models.FileField(upload_to='stage_images', blank=True, null=True, max_length=255)

    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)
