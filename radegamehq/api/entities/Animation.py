from django.db import models
from ..mixins.EntityBase import EntityBase


class Animation(EntityBase):
    delay = models.IntegerField(null=True, blank=True)
    repeat = models.IntegerField(null=True, blank=True, default=0)
    bidirectional = models.BooleanField(null=True, blank=True)

    type = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class AnimationStep(models.Model):
    owner = models.ForeignKey(Animation, blank=True, null=True, on_delete=models.CASCADE, related_name='steps')

    delay = models.IntegerField(null=True, blank=True)
    easing = models.CharField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)
    repeat = models.IntegerField(null=True, blank=True, default=0)
    bidirectional = models.BooleanField(null=True, blank=True)

    from_value = models.TextField(null=True, blank=True)
    to_value = models.TextField(null=True, blank=True)

    from_style_inline = models.TextField(null=True, blank=True)
    to_style_inline = models.TextField(null=True, blank=True)

    output_transformer = models.TextField(null=True, blank=True)
