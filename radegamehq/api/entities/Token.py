from django.db import models
from api.mixins.EntityBase import EntityBase, WithPermissions, WithCost, WithReveal


class Token(EntityBase, WithPermissions, WithCost, WithReveal):
    image = models.ImageField(upload_to='token_images', blank=True, null=True, max_length=None)

    attributes = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='attributes')

    def __str__(self):
        return self.name
