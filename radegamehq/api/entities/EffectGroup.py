from django.db import models

from .EffectStack import EffectStack
from api.mixins.EntityBase import EntityBase

MODE_CHOICES = (
    ('DRAW', 'DRAW'),
    ('TRIGGER', 'TRIGGER')
)

PICK_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)

QUOTA_CHOICES = (
    ('REPEATING', 'REPEATING'),
    ('ONCE', 'ONCE')
)


class EffectGroup(EntityBase):

    image = models.ImageField(upload_to='group_images', null=True, blank=True, max_length=None)

    mode = models.TextField(choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])

    min_cap = models.IntegerField(null=True, blank=True)
    max_cap = models.IntegerField(null=True, blank=True)
    random_cap = models.BooleanField(default=False)

    allow_same_pick = models.BooleanField(default=False)


class EffectGroupItem(models.Model):
    owner = models.ForeignKey(EffectGroup, on_delete=models.CASCADE)

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)

    cost = models.ManyToManyField(EffectStack, related_name='effect_item_cost')  # price to buy
    quota = models.IntegerField(default=1)  # how many will be available
    restriction = models.ManyToManyField(EffectStack, related_name='effect_item_restriction')
