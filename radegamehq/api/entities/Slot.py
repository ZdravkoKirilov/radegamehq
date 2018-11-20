from django.db import models

from api.mixins.EntityBase import EntityBase


class Slot(EntityBase):
    image = models.FileField(upload_to='slot_images', blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}".format(self.name)
