from ..mixins.EntityBase import EntityBase, WithDone, WithDisplayName


class Phase(EntityBase, WithDone, WithDisplayName):

    def __str__(self):
        return 'Phase_{}'.format(self.name)
