from walrus import Database, Model, TextField, ZSetField, IntegerField

db = Database()


class Lobby(Model):
    __database__ = db
    name = TextField(primary_key=True)
    mode = TextField()
    password = TextField()

    players = ZSetField()

    game = IntegerField()
    setup = IntegerField()
    owner = IntegerField()


class Player(Model):
    __database__ = db
    name = TextField(primary_key=True)  ## combination of game, lobbyname and playername
    team = IntegerField()
    faction = IntegerField()
    color = TextField()
