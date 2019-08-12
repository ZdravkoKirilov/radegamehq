from ..mixins.EntityBase import EntityBase, WithPermissions, WithCost, WithReveal


class Token(EntityBase, WithPermissions, WithCost, WithReveal):

    def __str__(self):
        return self.name
