from django.db import models

from api.mixins.EntityBase import EntityBase, WithPermissions, WithBoard, WithStakes, WithReveal, WithCost


class Condition(EntityBase, WithPermissions, WithBoard, WithStakes, WithReveal, WithCost):
    image = models.ImageField(upload_to='condition_images', blank=True, null=True, max_length=255)

    mode = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "{}".format(self.name)


class ConditionClause(models.Model):
    owner = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='clauses', blank=True, null=True)

    primary_clause = models.CharField(max_length=255, blank=False)

    secondary_clause = models.CharField(max_length=255, blank=True, null=True)

    negative = models.BooleanField(null=True, blank=True)

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='clause_condition',
                                  blank=True, null=True)
    action = models.ForeignKey('Action', on_delete=models.CASCADE,
                               blank=True, null=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, blank=True, null=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, blank=True, null=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, blank=True,
                                null=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE, blank=True,
                              null=True)
    phase = models.ForeignKey('Phase', on_delete=models.CASCADE, blank=True, null=True)
    round = models.ForeignKey('Round', on_delete=models.CASCADE, blank=True, null=True)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True)
    slot = models.ForeignKey('Slot', on_delete=models.CASCADE, blank=True, null=True)
    path = models.ForeignKey('Path', on_delete=models.CASCADE, blank=True, null=True)

    keywords = models.CharField(null=True, blank=True, max_length=255)

    amount = models.IntegerField(blank=True, null=True)

    relation = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)

# Do something at X round => can be done by composing 2 clauses: 1) the doing and 2) the circumstance
