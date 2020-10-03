from ..helpers.custom_file import ContentTypeRestrictedFileField
from ..mixins.EntityBase import EntityBase, WithModule


class Sound(EntityBase, WithModule):
    file = ContentTypeRestrictedFileField(
        upload_to='sounds',
        content_types=['application/ogg'],
        max_upload_size=5242880,
    )

    def __str__(self):
        return "{}".format(self.name)
