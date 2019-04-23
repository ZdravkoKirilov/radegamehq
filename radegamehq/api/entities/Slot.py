from django.db import models

from ..mixins.EntityBase import EntityBase, WithPermissions, WithBoard, WithKeywords, \
    WithStyle


class Slot(EntityBase, WithPermissions, WithBoard, WithKeywords, WithStyle):
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    field = models.ForeignKey('Field', null=True, blank=True, on_delete=models.SET_NULL)
    draw = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL, related_name='draw')

    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)
