from django.db import models

from ..helpers.custom_file import ContentTypeRestrictedFileField


class Sound(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    file = ContentTypeRestrictedFileField(
        upload_to='sounds',
        content_types=['application/ogg'],
        max_upload_size=5242880,
    )

    def __str__(self):
        return "{}".format(self.name)
