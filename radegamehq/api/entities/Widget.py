from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithFrame, WithStyle


class Widget(EntityBase, WithStyle):

    module = models.ForeignKey(
        "Module", on_delete=models.CASCADE, related_name='parent_module')

    node_getter = models.TextField(null=True, blank=True)
    render = models.TextField(null=True, blank=True)
    frame_getter = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class WidgetNode(WithBoard, WithStyle):

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    keywords = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(
        'Widget', on_delete=models.CASCADE, related_name="nodes")

    shape = models.ForeignKey(
        'Shape', null=True, blank=True, on_delete=models.SET_NULL)
    module = models.ForeignKey(
        'Module', null=True, blank=True, on_delete=models.SET_NULL)
    token = models.ForeignKey(
        'Token', null=True, blank=True, on_delete=models.SET_NULL)

    display_text = models.TextField(null=True, blank=True)
    display_text_inline = models.ForeignKey(
        'Text', null=True, blank=True, on_delete=models.SET_NULL)

    provide_context = models.TextField(null=True, blank=True)
    consume_context = models.TextField(null=True, blank=True)
    pass_to_children = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class NodeHandler(models.Model):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE,
                              related_name='handlers', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    sound = models.TextField(null=True, blank=True)
    static_sound = models.ForeignKey(
        'Sonata', null=True, blank=True, on_delete=models.SET_NULL)


class NodeLifecycle(models.Model):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE,
                              related_name='lifecycles', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    sound = models.TextField(null=True, blank=True)
    static_sound = models.ForeignKey(
        'Sonata', null=True, blank=True, on_delete=models.SET_NULL)


class WidgetFrame(WithFrame):
    owner = models.ForeignKey(
        Widget, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')
