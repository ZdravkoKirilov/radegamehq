from django.db import models
from api.mixins.EntityBase import EntityBase


class Phase(EntityBase):
    image = models.ImageField(upload_to='phase_images', blank=True, null=True, max_length=None)

    def __str__(self):
        return 'Phase_{}'.format(self.name)
