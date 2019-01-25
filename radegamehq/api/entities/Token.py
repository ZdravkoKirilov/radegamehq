from django.db import models
from api.mixins.EntityBase import EntityBase, WithPermissions, WithCost, WithReveal


class Token(EntityBase, WithPermissions, WithCost, WithReveal):

    attributes = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='attributes')

    def __str__(self):
        return self.name
