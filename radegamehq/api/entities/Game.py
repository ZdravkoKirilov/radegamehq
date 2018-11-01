from django.db import models

from api_auth.models import AppUser


class Game(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='game_images', blank=True, null=True, max_length=255)

    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    recommended_age = models.CharField(max_length=255, blank=True, null=True)

    fixed_teams = models.BooleanField(default=False)

    round_cycles = models.IntegerField(null=True, blank=True)

    round_order = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)
