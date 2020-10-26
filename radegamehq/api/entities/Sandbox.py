from django.db import models

from ..mixins.EntityBase import EntityBase


class Sandbox(EntityBase):
    global_state = models.TextField(blank=True, null=True)
    own_data = models.TextField(blank=True, null=True)
    on_init = models.TextField(blank=True, null=True)

    from_parent = models.TextField(blank=True, null=True)

    node = models.ForeignKey('WidgetNode', blank=True, null=True, on_delete=models.SET_NULL)
    module = models.ForeignKey('Module', blank=True, null=True, on_delete=models.SET_NULL)
    widget = models.ForeignKey('Widget', blank=True, null=True, on_delete=models.SET_NULL)
    token = models.ForeignKey('Token', blank=True, null=True, on_delete=models.SET_NULL)
