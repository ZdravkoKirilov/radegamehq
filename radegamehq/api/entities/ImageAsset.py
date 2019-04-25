from django.db import models
from sorl.thumbnail import ImageField

from ..entities.Game import Game


class ImageAsset(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    name = models.CharField(max_length=255)
    image = ImageField(upload_to='images', blank=True, null=True)

    svg = models.FileField(upload_to='svg_images', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
