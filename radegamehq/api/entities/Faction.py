from api.mixins.EntityBase import EntityBase, WithBoard


class Faction(EntityBase, WithBoard):

    def __str__(self):
        return self.name
