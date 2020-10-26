from django.db import models

from ..mixins.EntityBase import EntityBase, WithImage
from ..entities.Version import Version

class Setup(EntityBase, WithImage):

    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    recommended_age = models.IntegerField(null=True, blank=True)

    get_active_module = models.TextField()
    get_active_language = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
