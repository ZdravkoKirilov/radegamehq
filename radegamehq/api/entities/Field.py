from django.db import models

from ..mixins.EntityBase import EntityBase, WithCost, WithRisk, WithBoard, WithStakes


class Field(EntityBase, WithCost, WithRisk, WithBoard, WithStakes):
    image = models.ImageField(upload_to='field_images', blank=True, null=True, max_length=255)

    def __str__(self):
        return "{}".format(self.name)
