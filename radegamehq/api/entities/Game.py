from django.db import models

from api_auth.models import AppUser
from ..mixins.EntityBase import WithSettings


class Game(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='game_images', blank=True, null=True, max_length=255)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)



