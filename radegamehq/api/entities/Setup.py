from django.db import models


class Setup(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='setup_images', blank=True, null=True, max_length=None)

    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    recommended_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
