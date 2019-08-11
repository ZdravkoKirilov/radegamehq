from django.db import models


class Handler(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    type = models.CharField(max_length=255)

    state = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True, related_name='state')
    effect = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True, related_name='effect')

    def __str__(self):
        return "{}".format(self.name)
