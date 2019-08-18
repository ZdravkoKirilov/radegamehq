from api.mixins.EntityBase import EntityBase, WithBoard


class Team(EntityBase, WithBoard):

    def __str__(self):
        return self.name
