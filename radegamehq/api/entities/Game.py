from django.db import models

from api_auth.models import AppUser


class Game(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='game_images', blank=True, null=True, max_length=200)

    main_stage = models.OneToOneField('Stage', on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='main_stage')
    hide_factions = models.NullBooleanField(blank=True, null=True)

    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    recommended_age = models.CharField(max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class GlobalTermination(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)