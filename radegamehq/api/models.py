from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=False)
    boardType = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)
