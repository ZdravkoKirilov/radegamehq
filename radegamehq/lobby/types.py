from typing import Optional, Dict
from typing_extensions import Literal
from mypy_extensions import TypedDict


class LobbyType(TypedDict):
    name: str
    timestamp: int
    mode: Literal['private', 'public']
    password: Optional[str]

    game: int
    setup: int
    owner: int


class PlayerType(TypedDict):
    name: str
    lobby: str
    user: int

    data: Dict


class MessageType(TypedDict):
    id: str
    owner: int
    lobby: str

    message: str
    timestamp: int
