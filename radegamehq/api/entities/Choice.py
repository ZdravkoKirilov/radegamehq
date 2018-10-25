from django.db import models

from api.mixins.EntityBase import EntityBase
from .Stack import Stack


class Choice(EntityBase):
    image = models.ImageField(upload_to='choice_images', blank=True, null=True, max_length=200)

    options = models.ManyToManyField('ChoiceOption', related_name='choice_options')

    def __str__(self):
        return "{}".format(self.name)


class ChoiceOption(models.Model):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='choice_options')

    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='choice_option_images', blank=True, null=True, max_length=200)

    effect = models.ManyToManyField(Stack, related_name='choice_option_effects')

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
