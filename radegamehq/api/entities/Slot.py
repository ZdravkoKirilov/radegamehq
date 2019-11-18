from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithStyle, WithState, WithFrame


class Slot(EntityBase, WithBoard, WithStyle, WithState):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    x = models.IntegerField()
    y = models.IntegerField()

    shape = models.ForeignKey('Shape', null=True, blank=True, on_delete=models.SET_NULL)

    display_text = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='slot_display_text')

    populate_by = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

    enabled = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='slot_enabled')

    transitions = models.ManyToManyField('Transition', blank=True, related_name='transitionss_%(class)ss')

    def __str__(self):
        return "{}".format(self.name)


class SlotHandler(models.Model):
    owner = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='handlers', blank=True, null=True)
    handler = models.ForeignKey('Handler', on_delete=models.CASCADE)


class SlotItem(models.Model):
    owner = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    entity_type = models.CharField(max_length=255)

    action = models.ForeignKey('Action', null=True, blank=True, on_delete=models.CASCADE)
    condition = models.ForeignKey('Condition', null=True, blank=True, on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', null=True, blank=True, on_delete=models.CASCADE)
    token = models.ForeignKey('Token', null=True, blank=True, on_delete=models.CASCADE)


class SlotFrame(WithFrame):
    owner = models.ForeignKey(Slot, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
