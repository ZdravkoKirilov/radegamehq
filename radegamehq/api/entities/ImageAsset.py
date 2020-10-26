from django.db import models
from sorl.thumbnail import ImageField

from ..entities.Game import Game
from ..mixins.EntityBase import EntityBase, WithModule, WithImage


class ImageAsset(EntityBase, WithModule, WithImage):

    def __str__(self):
        return "{}".format(self.name)
