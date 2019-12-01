from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithFrame


class Slot(EntityBase, WithBoard):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    x = models.IntegerField()
    y = models.IntegerField()

    style = models.TextField(blank=True, null=True)
    style_inline = models.TextField(blank=True, null=True)

    shape = models.ForeignKey('Shape', null=True, blank=True, on_delete=models.SET_NULL)

    display_text = models.TextField(null=True, blank=True)

    populate_by = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

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
