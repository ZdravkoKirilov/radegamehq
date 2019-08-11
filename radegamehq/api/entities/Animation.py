from django.db import models


class Animation(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    from_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='from_style')
    to_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='to_style')

    def __str__(self):
        return "{}".format(self.name)
