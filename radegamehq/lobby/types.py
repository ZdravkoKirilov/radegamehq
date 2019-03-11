from typing import NamedTuple, Optional
from typing_extensions import Literal
from mypy_extensions import TypedDict


class LobbyType(TypedDict):
    name: str
    mode: Literal['private', 'public']
    password: Optional[str]

    game: int
    setup: int
    owner: int


class PlayerType(TypedDict):
    name: str
    lobby: str
    user: int
    game: int

    team: Optional[int]
    faction: Optional[int]
    color: Optional[int]
