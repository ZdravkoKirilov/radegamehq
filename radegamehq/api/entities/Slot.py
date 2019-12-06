from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithFrame, WithStyle


class Slot(EntityBase, WithBoard, WithStyle):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    x = models.IntegerField()
    y = models.IntegerField()

    shape = models.ForeignKey('Shape', null=True, blank=True, on_delete=models.SET_NULL)

    display_text = models.TextField(null=True, blank=True)

    transitions = models.ManyToManyField('Transition', blank=True, related_name='transitionss_%(class)ss')

    item = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class SlotHandler(models.Model):
    owner = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='handlers', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    sound = models.TextField(null=True, blank=True)


class SlotFrame(WithFrame):
    owner = models.ForeignKey(Slot, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
