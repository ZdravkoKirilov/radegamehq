from django.db import models
from sorl.thumbnail import ImageField

from ..entities.Game import Game


class ImageAsset(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    name = models.CharField(max_length=255)
    image = ImageField(upload_to='images')

    def __str__(self):
        return "{}".format(self.name)
