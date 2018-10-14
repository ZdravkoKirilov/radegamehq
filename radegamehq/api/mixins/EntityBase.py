from django.db import models

from api.entities.Game import Game


class EntityBase(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    keywords = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        abstract = True
