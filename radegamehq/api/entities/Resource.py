from django.db import models

from api.mixins.EntityBase import EntityBase


class Resource(models.Model, EntityBase):
    image = models.FileField(upload_to='resource_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)
