from django.db import models

from api.mixins.EntityBase import EntityBase

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT')
)

STACK_MODE = (
    ('PICK', 'PICK'),
    ('AUTO', 'AUTO')
)

QUOTA_CHOICES = (
    ('REPEATING', 'REPEATING'),
    ('ONCE', 'ONCE')
)

PICK_MODE = (
    ('RANDOM', 'RANDOM'),
    ('CHOICE', 'CHOICE')
)


class Stack(EntityBase):
    image = models.ImageField(upload_to='stack_images', null=True, blank=True, max_length=None)

    pick = models.CharField(choices=PICK_MODE, max_length=255, default=PICK_MODE[0][1])

    quota = models.CharField(choices=QUOTA_CHOICES, max_length=255, default=QUOTA_CHOICES[0][0])

    mode = models.CharField(choices=STACK_MODE, max_length=255, default=STACK_MODE[0][1])


class StackItem(models.Model):
    owner = models.ForeignKey(Stack, on_delete=models.CASCADE, related_name='stack_owner')

    action = models.ForeignKey('Action', on_delete=models.CASCADE, null=True, blank=True)
    condition = models.ForeignKey('Condition', on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, blank=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, null=True, blank=True)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, blank=True, null=True)

    amount = models.IntegerField(default=1, null=True, blank=True)
    max_amount = models.IntegerField(null=True, blank=True)
    min_amount = models.IntegerField(null=True, blank=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])

    def __str__(self):
        return 'Stack_{}_Item_{}'.format(self.owner.name, self.id)
