from django.db import models
from ..mixins.EntityBase import EntityBase, WithKeywords


class Text(EntityBase, WithKeywords):
    default_value = models.TextField()

    def __str__(self):
        return self.name


class Translation(models.Model):
    owner = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='translations')
    language = models.ForeignKey('GameLanguage', on_delete=models.CASCADE)

    value = models.TextField()

    def __str__(self):
        return self.lang
