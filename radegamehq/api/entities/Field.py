from ..mixins.EntityBase import EntityBase, WithCost, WithRisk, WithBoard, WithStakes


class Field(EntityBase, WithCost, WithRisk, WithBoard, WithStakes):

    def __str__(self):
        return "{}".format(self.name)
