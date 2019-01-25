from api.mixins.EntityBase import EntityBase, WithBoard, WithSettings, WithSetups


# type "Master" is not needed, action restriction/condition combined with keywords is enough:
#  the Master can have entirely different Actions


class Faction(EntityBase, WithBoard, WithSettings, WithSetups):

    def __str__(self):
        return self.name
