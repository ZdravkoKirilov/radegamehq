from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithFrame, WithStyle


class Widget(EntityBase):
    width = models.IntegerField()
    height = models.IntegerField()

    node_getter = models.TextField(null=True, blank=True)

    frame_getter = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class WidgetNode(EntityBase, WithBoard, WithStyle):
    owner = models.ForeignKey('Widget', on_delete=models.CASCADE, related_name="nodes")

    x = models.IntegerField()
    y = models.IntegerField()

    shape = models.ForeignKey('Shape', null=True, blank=True, on_delete=models.SET_NULL)

    display_text = models.TextField(null=True, blank=True)
    display_text_inline = models.ForeignKey('Text', null=True, blank=True, on_delete=models.SET_NULL)

    provide_context = models.TextField(null=True, blank=True)
    consume_context = models.TextField(null=True, blank=True)
    pass_to_children = models.TextField(null=True, blank=True)

    transitions = models.ManyToManyField('Transition', blank=True, related_name='transitionss_%(class)ss')

    item = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class NodeHandler(models.Model):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE, related_name='handlers', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    sound = models.TextField(null=True, blank=True)
    static_sound = models.ForeignKey('Sonata', null=True, blank=True, on_delete=models.SET_NULL)


class NodeLifecycle(models.Model):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE, related_name='lifecycles', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    sound = models.TextField(null=True, blank=True)
    static_sound = models.ForeignKey('Sonata', null=True, blank=True, on_delete=models.SET_NULL)


class WidgetFrame(WithFrame):
    owner = models.ForeignKey(Widget, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
