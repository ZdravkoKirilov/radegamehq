from django.db import models

from api.mixins.EntityBase import EntityBase, WithCost, WithCondition, WithPermissions, WithReveal, WithStakes, \
    WithSettings


class Choice(EntityBase, WithPermissions, WithCondition, WithCost, WithReveal, WithStakes):
    image = models.ImageField(upload_to='choice_images', blank=True, null=True, max_length=None)

    mode = models.CharField(max_length=255)
    random = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ChoiceOption(WithSettings):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='options', null=True, blank=True)

    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    keywords = models.CharField(null=True, blank=True, max_length=255)

    image = models.ImageField(upload_to='choice_option_images', blank=True, null=True, max_length=None)

    effect = models.ManyToManyField('Source', blank=True)
    value = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
