from walrus import Database, Model, TextField, IntegerField, JSONField

db = Database(host="localhost", port=6379, charset="utf-8", decode_responses=True)

MODES = (
    ('public', 'public'),
    ('private', 'private')
)


class Lobby(Model):
    __database__ = db
    name = TextField(primary_key=True)
    timestamp = IntegerField()
    mode = TextField()
    password = TextField()

    game = IntegerField(index=True)
    setup = IntegerField()
    owner = IntegerField()


class Player(Model):
    __database__ = db
    name = TextField(primary_key=True)  ## combination of game, lobbyname and playername
    lobby = TextField(index=True)
    user = IntegerField()
    game = IntegerField()

    data = JSONField()
