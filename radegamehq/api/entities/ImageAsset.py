from django.db import models
from sorl.thumbnail import ImageField

from ..entities.Game import Game
from ..mixins.EntityBase import EntityBase, WithModule


class ImageAsset(EntityBase, WithModule):
    image = ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
