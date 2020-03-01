from django.db import models
from ..mixins.EntityBase import EntityBase, WithStyle


class Text(EntityBase, WithStyle):
    default_value = models.TextField()

    def __str__(self):
        return self.name


class Translation(models.Model):
    owner = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='translations', blank=True, null=True)
    language = models.ForeignKey('GameLanguage', on_delete=models.CASCADE)

    value = models.TextField()

    def __str__(self):
        return self.lang
