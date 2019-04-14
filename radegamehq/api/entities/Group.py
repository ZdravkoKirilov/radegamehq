from django.db import models

from ..mixins.EntityBase import EntityBase, WithPermissions, WithCost, WithSetups

RELATIONS = (
    ('NONE', 'NONE'),
    ('AND', 'AND'),
    ('OR', 'OR')
)


class Group(EntityBase, models.Model):
    def __str__(self):
        return "{}".format(self.name)


class GroupItem(WithPermissions, WithCost, WithSetups):
    owner = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, related_name='items')

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)

    amount = models.IntegerField(default=1)

    relation = models.CharField(choices=RELATIONS, max_length=255, default=RELATIONS[0][0])

    def __str__(self):
        return "{}".format(self.name)
