from django.db import models

from api.mixins.EntityBase import EntityBase


class Resource(EntityBase):
    image = models.FileField(upload_to='resource_images', blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}".format(self.name)
