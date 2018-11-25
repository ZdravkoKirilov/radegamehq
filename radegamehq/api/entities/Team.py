from django.db import models

from api.mixins.EntityBase import EntityBase, WithBoard, WithSettings


class Team(EntityBase, WithBoard, WithSettings):
    image = models.ImageField(upload_to='team_images', blank=True, null=True, max_length=None)

    def __str__(self):
        return self.name
