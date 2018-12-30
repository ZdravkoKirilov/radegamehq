from django.db import models

from api.mixins.EntityBase import EntityBase, WithPermissions, WithBoard, WithRisk, WithSettings


class Slot(EntityBase, WithPermissions, WithBoard, WithRisk, WithSettings):
    image = models.ImageField(upload_to='slot_images', blank=True, null=True, max_length=255)
    owner = models.ForeignKey('Stage', on_delete=models.CASCADE)

    field = models.ForeignKey('Field', null=True, blank=True, on_delete=models.SET_NULL)
    draw = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL, related_name='draw')

    revealed = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL)

    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    shape = models.CharField(max_length=255, blank=True, null=True)
    points = models.CharField(max_length=510, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
