from django.db import models

from api.entities.Game import Game


class Stage(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='stage_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)