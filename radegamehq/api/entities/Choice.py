from django.db import models

from ..mixins.EntityBase import EntityBase, WithCost, WithCondition, WithPermissions, WithReveal, WithStakes, \
    WithSettings
from ..entities.ImageAsset import ImageAsset


class Choice(EntityBase, WithPermissions, WithCondition, WithCost, WithReveal, WithStakes):
    mode = models.CharField(max_length=255)
    random = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ChoiceOption(WithSettings):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='options', null=True, blank=True)

    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    keywords = models.CharField(null=True, blank=True, max_length=255)

    image = models.ForeignKey(ImageAsset, blank=True, null=True, on_delete=models.SET_NULL)

    effect = models.ManyToManyField('Source', blank=True)
    value = models.CharField(null=True, blank=True, max_length=255)
    secret = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
