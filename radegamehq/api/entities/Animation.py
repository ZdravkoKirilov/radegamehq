from django.db import models


class Animation(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    type = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class AnimationStep(models.Model):
    owner = models.ForeignKey(Animation, blank=True, null=True, on_delete=models.CASCADE, related_name='steps')

    delay = models.IntegerField(null=True, blank=True)
    easing = models.CharField(max_length=255)

    from_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='from_style')
    to_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='to_style')
