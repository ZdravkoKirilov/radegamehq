from django.db import models

from api.mixins.EntityBase import EntityBase


class Field(EntityBase):
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=255)

    cost = models.ManyToManyField('Source', related_name='field_cost', blank=True)

    done = models.ManyToManyField('Source', related_name='field_award', blank=True)
    undone = models.ManyToManyField('Source', related_name='field_penalty', blank=True)

    stage = models.ForeignKey('Stage', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.name)
