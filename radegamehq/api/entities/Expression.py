from django.db import models


class Expression(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    code = models.TextField(max_length=None)

    def __str__(self):
        return "{}".format(self.name)
