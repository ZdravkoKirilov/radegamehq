from django.db import models


class EntityBase(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.name)

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


class ImageFrame(models.Model):
    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True)

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


class WithPermissions(models.Model):
    enable = models.ManyToManyField('Condition', blank=True, related_name='enable_%(class)ss')
    disable = models.ManyToManyField('Condition', blank=True, related_name='disable_%(class)ss')

    class Meta:
        abstract = True


class WithSettings(models.Model):
    settings = models.ManyToManyField('Condition', blank=True, related_name='settings_%(class)ss')

    class Meta:
        abstract = True


class WithBoard(models.Model):
    board = models.ForeignKey('Stage', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='board_%(class)ss')

    class Meta:
        abstract = True


class WithStakes(models.Model):
    done = models.ManyToManyField('Expression', blank=True, related_name='done_%(class)ss')
    undone = models.ManyToManyField('Expression', blank=True, related_name='undone_%(class)ss')

    class Meta:
        abstract = True


class WithRisk(models.Model):
    risk = models.ManyToManyField('Expression', blank=True, related_name='risk_%(class)ss')

    class Meta:
        abstract = True


class WithCondition(models.Model):
    condition = models.ManyToManyField('Condition', blank=True, related_name='condition_%(class)ss')

    class Meta:
        abstract = True


class WithCost(models.Model):
    cost = models.ManyToManyField('Expression', blank=True, related_name='cost_%(class)ss')

    class Meta:
        abstract = True


class WithReveal(models.Model):
    reveal_cost = models.ManyToManyField('Expression', blank=True, related_name='reveal_cost_%(class)ss')
    reveal_slots = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class WithSetups(models.Model):
    setups = models.ManyToManyField('Setup', blank=True, related_name='setups_%(class)ss')

    class Meta:
        abstract = True
