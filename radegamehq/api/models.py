from django.db import models


class Game(models.Model):
    TYPE_TERRITORY_MAP = 'MAP'
    TYPE_BASIC_GRID = 'BASIC_GRID'

    TYPE_CHOICES = (
        (TYPE_TERRITORY_MAP, 'MAP'),
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
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class MapLocation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    width = models.IntegerField()
    height = models.IntegerField()
    left = models.IntegerField()
    top = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    field = models.OneToOneField(
        BoardField,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.field.name)


class Map(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='maps', blank=True, null=True, max_length=200)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format('Map_') + self.game.title


class MapPath(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    fromLoc = models.ForeignKey(
        MapLocation,
        related_name='from_loc+',
        on_delete=models.CASCADE,
    )
    toLoc = models.ForeignKey(
        MapLocation,
        related_name='to_loc+',
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format('From: ' + self.fromLoc.field.name + ' To: ' + self.toLoc.field.name)
