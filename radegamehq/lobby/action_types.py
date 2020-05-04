from enum import Enum


class LobbyActionTypes(Enum):
    FETCH_LOBBIES = '[Lobby] FETCH_LOBBIES'
    ADD_LOBBIES = '[Lobby] ADD_LOBBIES'
    CREATE_LOBBY = '[Lobby] CREATE_LOBBY'
    ADD_LOBBY = '[Lobby] ADD_LOBBY'
    DELETE_LOBBY = '[Lobby] DELETE_LOBBY'
    REMOVE_LOBBY = '[Lobby] REMOVE_LOBBY'

    SAVE_PLAYER = '[Lobby] SAVE_PLAYER'
    ADD_PLAYER = '[Lobby] ADD_PLAYER'
    DELETE_PLAYER = '[Lobby] DELETE_PLAYER'
    REMOVE_PLAYER = '[Lobby] REMOVE_PLAYER'

    SEND_MESSAGE = '[Lobby] SEND_MESSAGE'
    ADD_MESSAGE = '[Lobby] ADD_MESSAGE'

    CREATE_GAME = '[Lobby] CREATE_GAME'
    START_GAME = '[Lobby] START_GAME'
