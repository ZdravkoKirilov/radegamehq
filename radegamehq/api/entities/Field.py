from ..mixins.EntityBase import EntityBase, WithBoard, WithStakes


class Field(EntityBase, WithBoard, WithStakes):

    def __str__(self):
        return "{}".format(self.name)
