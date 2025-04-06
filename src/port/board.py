from typing import Self

from .player import Player

BLANK = "."
RED = "r"
YELLOW = "y"

Tile = Player | None
Row = list[Tile]

class Board:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

        self._board: list[Row] = [[None] * width for _ in range(height)]

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def copy(self) -> Self:
        cpy = Board(self.width, self.height)

        for col in range(self.width):
            for row in range(self.height):
                tile = self.get_tile(col, row)
                cpy.set_tile(col, row, tile)

        return cpy

    def column_free(self, x: int) -> bool:
        return self.get_tile(x, self.height - 1) == None

    def drop_column(self, x: int, player: Player) -> tuple[int, int]:

        if not self.column_free(x):
            raise RuntimeError(f"Tried to drop in full column {x}")

        for y in range(self.height):
            if self.get_tile(x, y) == None:
                self.set_tile(x, y, player)
                return x, y

    def get_tile(self, x: int, y: int) -> Tile:
        """
        0, 0 bottom left
        """
        return self._board[self.height - y - 1][x]

    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        self._board[self.height - y - 1][x] = tile

    def __str__(self) -> str:
        s = ""

        for row in self._board:
            s += "".join(" " if t is None else t.to_c() for t in row)
            s += "\n"

        return s
