from django.db import models

from ..mixins.EntityBase import EntityBase


class Sonata(EntityBase):

    type = models.TextField()

    loop = models.NullBooleanField()

    def __str__(self):
        return "{}".format(self.name)


class SonataStep(models.Model):
    owner = models.ForeignKey(Sonata, blank=True, null=True, on_delete=models.CASCADE, related_name='steps')

    sound = models.ForeignKey('Sound', on_delete=models.CASCADE)

    volume = models.FloatField(null=True, blank=True)
    loop = models.NullBooleanField()
    rate = models.FloatField(null=True, blank=True)
