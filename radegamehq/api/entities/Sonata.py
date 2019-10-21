from django.db import models


class Sonata(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    type = models.TextField()

    loop = models.NullBooleanField()

    def __str__(self):
        return "{}".format(self.name)


class SonataStep(models.Model):
    owner = models.ForeignKey(Sonata, blank=True, null=True, on_delete=models.CASCADE, related_name='steps')

    sound = models.ForeignKey('Sound', on_delete=models.CASCADE)

    volume = models.FloatField(null=True, blank=True)
    loop = models.NullBooleanField()
    rate = models.FloatField(null=True, blank=True)
