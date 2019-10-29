from django.db import models


class Shape(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    type = models.TextField()

    construct_by = models.ForeignKey('Expression', on_delete=models.SET_NULL, blank=True, null=True)
    construct_by_inline = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ShapePoint(models.Model):
    owner = models.ForeignKey(Shape, blank=True, null=True, on_delete=models.CASCADE, related_name='points')

    x = models.CharField(max_length=255)
    y = models.CharField(max_length=255)
