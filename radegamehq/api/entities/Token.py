from django.db import models
from ..mixins.EntityBase import EntityBase, WithTemplate, WithText, WithModule, WithKeywords, WithImage, WithShape, WithWidget


class Token(EntityBase, WithTemplate, WithModule, WithKeywords):

    def __str__(self):
        return self.name


class TokenNode(EntityBase, WithImage, WithText, WithWidget, WithShape):
    owner = models.ForeignKey(
        Token, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
