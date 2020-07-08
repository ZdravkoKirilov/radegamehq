from django.db import models
from ..mixins.EntityBase import EntityBase, WithFrame, WithTemplate, WithText


class Token(EntityBase, WithTemplate):

    def __str__(self):
        return self.name


class TokenFrame(WithFrame):
    owner = models.ForeignKey(
        Token, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')


class TokenText(WithText):
    owner = models.ForeignKey(
        Token, blank=True, null=True, on_delete=models.CASCADE, related_name='texts')
