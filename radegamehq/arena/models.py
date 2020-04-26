from django.db import models
import uuid

from api.entities.Game import Game
from api.entities.Faction import Faction
from api.entities.Setup import Setup
from api_auth.models import AppUser


class GameInstance(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    public_id = models.CharField(max_length=255, null=True, blank=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    state = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = str(uuid.uuid4())
        return super(GameInstance, self).save(*args, **kwargs)


class GamePlayer(models.Model):
    owner = models.ForeignKey(GameInstance, on_delete=models.CASCADE, null=True, blank=True, related_name='players')

    name = models.CharField(max_length=255)
    user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, blank=True, null=True)
