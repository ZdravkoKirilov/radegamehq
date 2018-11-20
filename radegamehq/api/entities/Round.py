from django.db import models

from api.mixins.EntityBase import EntityBase


class Round(EntityBase):
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, blank=True, null=True, related_name="round_stage")

    image = models.ImageField(upload_to='round_images', blank=True, null=True, max_length=None)

    replay_count = models.IntegerField(null=True, blank=True)  # how many tries to pass the condition
    repeat = models.IntegerField(null=True, blank=True)  # repeat X times before going to the next round

    phases = models.ManyToManyField('Phase', related_name='round_phases')
    phase_order = models.TextField(null=True, blank=True)

    condition = models.ManyToManyField('Condition', related_name='round_condition')

    undone = models.ManyToManyField('Source', related_name='round_penalty')
    done = models.ManyToManyField('Source', related_name='round_award')

    def __str__(self):
        return "{}".format(self.name)
