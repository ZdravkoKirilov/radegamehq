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


class Resource(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='resource_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class BoardField(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    income = models.ManyToManyField(Resource, through='FieldIncome')

    def __str__(self):
        return "{}".format(self.name)


class FieldIncome(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.field.name, self.resource.name)

class MapLocation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    width = models.FloatField()
    height = models.FloatField()
    left = models.FloatField()
    top = models.FloatField()
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
