from django.db import models

from api.mixins.EntityBase import EntityBase


class Stage(models.Model, EntityBase):
    image = models.FileField(upload_to='stage_images', blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}".format(self.name)
