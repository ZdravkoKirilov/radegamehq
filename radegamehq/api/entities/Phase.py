from django.db import models
from api.mixins.EntityBase import EntityBase, WithSettings


class Phase(EntityBase, WithSettings):
    image = models.ImageField(upload_to='phase_images', blank=True, null=True, max_length=None)

    turn_cycles = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return 'Phase_{}'.format(self.name)
