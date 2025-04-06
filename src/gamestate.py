import threading

from .port.alpha_beta import connect_four_ab
from .port.evals import utility
from .port.board import Board, Tile
from .port.player import Player

class GameState:
    def __init__(self, width: int, height: int, play_as: Player, depth: int):

        self._width = width
        self._height = height

        self.reset(play_as, depth)

    def reset(self, play_as: Player, depth: int) -> None:
        self._board = Board(self._width, self._height)
        self._cursor = self._width // 2  # for dropping

        self._can_play = True
        self._game_over = False
        self._play_as = play_as
        self._depth = depth

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def cursor(self) -> int:
        return self._cursor

    @property
    def playing_as(self) -> Player:
        return self._play_as

    def tile_at(self, x: int, y: int) -> Tile:
        return self._board.get_tile(x, y)

    def try_move_left(self) -> None:
        if self._cursor > 0:
            self._cursor -= 1

    def try_move_right(self) -> None:
        if self._cursor < self._width - 1:
            self._cursor += 1

    def try_drop(self) -> None:

        if not self._can_play or not self._board.column_free(self._cursor):
            return

        self._board.drop_column(self._cursor, self.playing_as)
        self._can_play = False

        if utility(self._board) != 0:
            self._game_over = True
            # player won! TODO
            return

        # else play on
        machine_move = threading.Thread(target=self.ai_move)
        machine_move.start()


    def ai_move(self) -> None:

        cpy = self._board.copy()

        ai_player = self.playing_as.opposite()

        play = connect_four_ab(cpy, ai_player, self._depth)
        self._board.drop_column(play, ai_player)

        if utility(self._board) != 0:  # ai won :(
            self._game_over = True
            return

        # otherwise play on
        self._can_play = True


    def try_restart(self) -> None:  # TODO
        if self._game_over:
            self.reset(self.playing_as, self._depth)
