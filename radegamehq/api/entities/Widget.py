from django.db import models

from ..mixins.EntityBase import EntityBase, WithBoard, WithFrame, WithStyle, WithModule


class Widget(EntityBase, WithStyle):

    module = models.ForeignKey(
        "Module", on_delete=models.CASCADE, related_name='parent_module')

    get_nodes = models.TextField(null=True, blank=True)
    render = models.TextField(null=True, blank=True)
    dynamic_background = models.TextField(null=True, blank=True)
    background = models.ForeignKey(
        'ImageAsset', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class WidgetNode(WithBoard, WithStyle):
    owner = models.ForeignKey(
        'Widget', on_delete=models.CASCADE, related_name="nodes")

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    shape = models.ForeignKey(
        'Shape', null=True, blank=True, on_delete=models.SET_NULL)
    module = models.ForeignKey(
        'Module', null=True, blank=True, on_delete=models.SET_NULL)
    token = models.ForeignKey(
        'Token', null=True, blank=True, on_delete=models.SET_NULL)
    widget = models.ForeignKey(
        'Widget', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(
        'ImageAsset', null=True, blank=True, on_delete=models.SET_NULL)

    dynamic_text = models.TextField(null=True, blank=True)
    text = models.ForeignKey(
        'Text', null=True, blank=True, on_delete=models.SET_NULL)

    provide_context = models.TextField(null=True, blank=True)
    consume_context = models.TextField(null=True, blank=True)
    pass_to_children = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class NodeHandler(EntityBase):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE,
                              related_name='handlers', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    dynamic_sound = models.TextField(null=True, blank=True)
    sound = models.ForeignKey(
        'Sonata', null=True, blank=True, on_delete=models.SET_NULL)


class NodeLifecycle(EntityBase):
    owner = models.ForeignKey(WidgetNode, on_delete=models.CASCADE,
                              related_name='lifecycles', blank=True, null=True)

    type = models.CharField(max_length=255)

    effect = models.TextField(null=True, blank=True)

    dynamic_sound = models.TextField(null=True, blank=True)
    sound = models.ForeignKey(
        'Sonata', null=True, blank=True, on_delete=models.SET_NULL)
