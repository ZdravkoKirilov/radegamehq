from django.db import models


class Stage(models.Model):
    image = models.FileField(upload_to='stage_images', blank=True, null=True, max_length=255)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    keywords = models.CharField(null=True, blank=True, max_length=255)

    width: models.IntegerField()
    height: models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)
