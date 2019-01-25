from api.mixins.EntityBase import EntityBase, WithBoard, WithSettings


class Team(EntityBase, WithBoard, WithSettings):

    def __str__(self):
        return self.name
