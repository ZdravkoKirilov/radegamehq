from django.db import models

from api.mixins.EntityBase import EntityBase

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT')
)

PICK_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)


class Stack(EntityBase):
    image = models.ImageField(upload_to='stack_images', null=True, blank=True, max_length=None)
    pick = models.CharField(choices=PICK_CHOICES, max_length=255, default=PICK_CHOICES[0][0])


class StackItem(models.Model):
    owner = models.ForeignKey(Stack, on_delete=models.CASCADE, related_name='stack_owner')

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, blank=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])
