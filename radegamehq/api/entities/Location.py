from django.db import models

from ..entities.Field import Field
from ..mixins.EntityBase import EntityBase


class Location(EntityBase):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    image = models.FileField(upload_to='location_images', blank=True, null=True, max_length=None)

    width = models.FloatField()
    height = models.FloatField()

    x = models.FloatField()
    y = models.FloatField()

    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True, blank=True)
    tokens = models.ManyToManyField('Token',  blank=True)

    allowed = models.ManyToManyField('Stack', blank=True, related_name='allowed')
    restricted = models.ManyToManyField('Stack', blank=True)

    def __str__(self):
        return "{}".format(self.name)
