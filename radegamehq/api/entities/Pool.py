from django.db import models

from .Stack import Stack
from api.mixins.EntityBase import EntityBase

MODE_CHOICES = (
    ('DRAW', 'DRAW'),
    ('AUTO', 'AUTO')
)

PICK_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)

QUOTA_CHOICES = (
    ('REPEATING', 'REPEATING'),
    ('ONCE', 'ONCE')
)


class Pool(EntityBase):

    image = models.ImageField(upload_to='pool_images', null=True, blank=True, max_length=None)

    mode = models.TextField(choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])

    min_cap = models.IntegerField(null=True, blank=True)
    max_cap = models.IntegerField(null=True, blank=True)
    random_cap = models.BooleanField(default=False)

    allow_same_pick = models.BooleanField(default=False)


class PoolItem(models.Model):
    owner = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="items")

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, blank=True)

    quota = models.IntegerField(default=1)  # how many will be available

    cost = models.ManyToManyField(Stack, related_name='pool_item_cost')  # price to buy
    restricted = models.ManyToManyField(Stack, related_name='pool_item_restricted')
    allowed = models.ManyToManyField(Stack, related_name='pool_item_allowed')

    def __str__(self):
        return 'Pool_{}_Item_{}'.format(self.owner.name, self.id)
