from django.db import models


class EntityBase(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)

    keywords = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        abstract = True


class WithImage(models.Model):
    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class WithStyle(models.Model):
    style = models.TextField(blank=True, null=True)
    style_inline = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class WithKeywords(models.Model):
    keywords = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class WithBoard(models.Model):
    board = models.ForeignKey('Widget', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='board_%(class)ss')

    class Meta:
        abstract = True


class WithTemplate(models.Model):
    template = models.ForeignKey('Widget', blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='template_%(class)ss')

    class Meta:
        abstract = True


class WithFrame(WithStyle):
    name = models.TextField(blank=True, null=True)

    image = models.ForeignKey('ImageAsset', on_delete=models.CASCADE, blank=True, null=True,
                              related_name='image_%(class)ss')
    widget = models.ForeignKey('Widget', on_delete=models.CASCADE, blank=True, null=True, related_name='widget_%(class)ss')

    class Meta:
        abstract = True


class WithText(WithStyle):
    name = models.TextField(blank=True, null=True)
    text = models.ForeignKey('Text', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True
