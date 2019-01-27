from django.db import models

from ..mixins.EntityBase import EntityBase, WithPermissions, WithCost, WithCondition, WithReveal, WithStakes


class Action(EntityBase, WithPermissions, WithCost, WithCondition, WithReveal, WithStakes):
    mode = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class ActionConfig(models.Model):
    owner = models.ForeignKey(Action, blank=True, null=True, on_delete=models.CASCADE, related_name='configs')

    type = models.CharField(max_length=255, blank=False)
    target = models.CharField(max_length=255, blank=False)
    target_filter = models.CharField(max_length=255, blank=True, null=True)

    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True,
                                  blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True,
                               blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, null=True,
                                blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True,
                              blank=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='action_config_action', blank=True,
                               null=True)

    keywords = models.CharField(max_length=255, null=True, blank=True)

    value = models.CharField(null=True, blank=True, max_length=255)
    computed_value = models.CharField(null=True, blank=True, max_length=255)

    amount = models.IntegerField(blank=True, null=True, default=0)
    max_amount = models.IntegerField(blank=True, null=True, default=0)
    min_amount = models.IntegerField(blank=True, null=True, default=0)
    random_amount = models.BooleanField(blank=True, null=True, default=False)
    dice_amount = models.ForeignKey('Choice', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='action_dice_amount')

    def __str__(self):
        return "Config_{}_{}".format(self.owner.name, self.type)
