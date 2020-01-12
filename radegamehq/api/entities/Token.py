from django.db import models
from ..mixins.EntityBase import EntityBase, WithFrame


class Token(EntityBase):

    def __str__(self):
        return self.name


class TokenFrame(WithFrame):
    owner = models.ForeignKey(Token, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
