from ..mixins.EntityBase import EntityBase


class Faction(EntityBase):

    def __str__(self):
        return self.name
