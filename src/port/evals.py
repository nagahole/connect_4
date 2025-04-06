from .board import Board
from .player import Player


def utility(board: Board) -> int:

    if num_in_a_row(4, board, Player.RED):
        return 10000
    elif num_in_a_row(4, board, Player.YELLOW):
        return -10000

    return 0

def evaluate(board: Board) -> int:
    return score(board, Player.RED) - score(board, Player.YELLOW)

def score(board: Board, player: Player) -> int:

    util = utility(board)

    if util != 0:
        return util

    res = 0

    for consec in range(1, 4):  # 1 2 3
        res += 10 ** min(consec - 1, 3) * num_in_a_row(consec, board, player)

    return res


def num_in_a_row(count: int, board: Board, player: Player) -> int:

    width = board.width
    height = board.height

    res = 0

    for x in range(width):
        for y in range(height):

            # only checks if tile matches player
            if board.get_tile(x, y) != player:
                continue

            # horizontal
            if x + count <= width and all(board.get_tile(x + i, y) == player for i in range(count)):
                res += 1

            # vertical
            if y + count <= height and all(board.get_tile(x, y + i) == player for i in range(count)):
                res += 1

            # diagonal up
            if x + count <= width and y + count <= height and all(board.get_tile(x + i, y + i) == player for i in range(count)):
                res += 1

            # diagonal down
            if x + count <= width and y - count >= -1 and all(board.get_tile(x + i, y - i) == player for i in range(count)):
                res += 1

    return res
