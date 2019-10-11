from django.db import models


class Animation(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    delay = models.IntegerField(null=True, blank=True)
    repeat = models.IntegerField(null=True, blank=True, default=0)
    bidirectional = models.BooleanField(null=True, blank=True)

    type = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class AnimationStep(models.Model):
    owner = models.ForeignKey(Animation, blank=True, null=True, on_delete=models.CASCADE, related_name='steps')

    delay = models.IntegerField(null=True, blank=True)
    easing = models.CharField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)
    repeat = models.IntegerField(null=True, blank=True, default=0)
    bidirectional = models.BooleanField(null=True, blank=True)

    from_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='from_style')
    to_style = models.ForeignKey('Style', on_delete=models.CASCADE, related_name='to_style')
