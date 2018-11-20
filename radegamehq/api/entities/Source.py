from django.db import models

from ..mixins.EntityBase import EntityBase

MODE_CHOICES = (
    ('DRAW', 'DRAW'),
    ('AUTO', 'AUTO'),
    ('PASSIVE', 'PASSIVE'),
)

PICK_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)

QUOTA_CHOICES = (
    ('ONCE', 'ONCE'),
    ('ON_TURN', 'ON_TURN'),
    ('ON_PHASE', 'ON_PHASE'),
    ('ON_ROUND', 'ON_ROUND')
)

RELATIONS = (
    ('NONE', 'NONE'),
    ('AND', 'AND'),
    ('OR', 'OR')
)


class Source(EntityBase):
    image = models.ImageField(upload_to='source_images', null=True, blank=True, max_length=None)

    mode = models.TextField(choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])


class SourceItem(models.Model):
    owner = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="items")

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)

    amount = models.IntegerField(default=1)

    cost = models.ManyToManyField(Source, related_name='source_item_cost')  # price to buy

    restricted = models.ManyToManyField('Condition', related_name='source_item_restricted')
    allowed = models.ManyToManyField('Condition', related_name='source_item_allowed')

    relation = models.CharField(choices=RELATIONS, max_length=255, default=RELATIONS[0][0])

    def __str__(self):
        return 'Source_{}:Item_{}'.format(self.owner.name, self.id)
