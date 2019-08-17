from ..mixins.EntityBase import EntityBase, WithDisplayName


class Keyword(EntityBase, WithDisplayName):

    def __str__(self):
        return "{}".format(self.name)
