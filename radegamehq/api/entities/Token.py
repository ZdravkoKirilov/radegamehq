from django.db import models
from ..mixins.EntityBase import EntityBase, WithKeywords


class Token(EntityBase, WithKeywords):
    value = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
