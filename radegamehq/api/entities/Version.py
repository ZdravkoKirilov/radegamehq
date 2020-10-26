from django.db import models

from ..mixins.EntityBase import WithGame, EntityBase


class Version(EntityBase, WithGame):

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    menu = models.ForeignKey(
        'Module', on_delete=models.SET_NULL, related_name='menu', null=True, blank=True)
