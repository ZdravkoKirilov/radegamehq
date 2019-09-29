from django.db import models


class Transition(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    trigger = models.TextField()
    prop = models.CharField(max_length=255)

    animation = models.ForeignKey('Animation', on_delete=models.CASCADE, related_name='animation', blank=True, null=True)
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE, related_name='sound', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
