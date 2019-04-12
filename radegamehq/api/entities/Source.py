from django.db import models

from ..mixins.EntityBase import EntityBase
from ..entities.Group import Group

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


class Source(EntityBase):
    mode = models.TextField(choices=MODE_CHOICES, default=MODE_CHOICES[0][0])

    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
