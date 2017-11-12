from django.db import models


class Game(models.Model):
    TYPE_TERRITORY_MAP = 'TERRITORY_MAP'
    TYPE_BASIC_GRID = 'BASIC_GRID'

    TYPE_CHOICES = (
        (TYPE_TERRITORY_MAP, 'TERRITORY_MAP'),
        (TYPE_BASIC_GRID, 'BASIC_GRID'),
    )

    title = models.CharField(max_length=255, blank=False)
    boardType = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class BoardField(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='field_images', blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    asMapItem = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
