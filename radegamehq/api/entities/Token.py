from django.db import models
from ..mixins.EntityBase import EntityBase, WithKeywords, WithFrame


class Token(EntityBase, WithKeywords):
    value = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class TokenFrame(WithFrame):
    owner = models.ForeignKey(Token, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
