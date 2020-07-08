from django.db import models


class Version(models.Model):
    def __str__(self):
        return self.name

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.TextField()
