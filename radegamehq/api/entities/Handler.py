from django.db import models

from ..mixins.EntityBase import WithState


class Handler(WithState, models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='handler_effect')

    enabled = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='handler_enabled')

    def __str__(self):
        return "{}".format(self.name)
