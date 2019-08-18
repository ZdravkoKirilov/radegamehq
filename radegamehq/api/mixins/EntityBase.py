from django.db import models


class EntityBase(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        abstract = True


class WithImage(models.Model):
    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class WithDone(models.Model):
    done = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class WithDisplayName(models.Model):
    display_name = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class WithType(models.Model):
    entity_type = models.CharField(max_length=255)

    class Meta:
        abstract = True


class WithState(models.Model):
    state = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='state_%(class)ss')

    class Meta:
        abstract = True


class WithStyle(models.Model):
    style = models.ForeignKey('Style', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='style_%(class)ss')

    class Meta:
        abstract = True


class WithKeywords(models.Model):
    keywords = models.ManyToManyField('Keyword', blank=True, related_name='keywords_%(class)ss')

    class Meta:
        abstract = True


class WithBoard(models.Model):
    board = models.ForeignKey('Stage', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='board_%(class)ss')

    class Meta:
        abstract = True


class WithStakes(models.Model):
    passes = models.ForeignKey('Expression', blank=True, null=True, related_name='passes_%(class)ss',
                               on_delete=models.SET_NULL)
    fails = models.ForeignKey('Expression', blank=True, null=True, related_name='fails_%(class)ss',
                              on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class WithFrame(models.Model):
    image = models.ForeignKey('ImageAsset', on_delete=models.CASCADE, related_name='frame_%(class)ss')

    class Meta:
        abstract = True
