from django.db import models

from api_auth.models import AppUser
from ..mixins.EntityBase import WithImage


class Game(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, db_index=True, unique=True)
    image = models.ImageField(upload_to='game_images', blank=True, null=True, max_length=255)

    description = models.TextField(blank=True, null=True)

    get_active_language = models.TextField(blank=True, null=True)

    menu = models.ForeignKey('Widget', blank=True, null=True, on_delete=models.SET_NULL, related_name='menu')

    def __str__(self):
        return "{}".format(self.title)


class GameLanguage(WithImage):
    owner = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='languages', blank=True, null=True)
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
