from django.db import models

from ..mixins.EntityBase import EntityBase
from ..entities.ImageAsset import ImageAsset


class Choice(EntityBase):
    random = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ChoiceOption(models.Model):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='options', null=True, blank=True)

    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)

    image = models.ForeignKey(ImageAsset, blank=True, null=True, on_delete=models.SET_NULL)

    effect = models.ForeignKey('Expression', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
