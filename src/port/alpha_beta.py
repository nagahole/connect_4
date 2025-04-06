from .board import Board
from .player import Player
from .evals import *

def connect_four_ab(board: Board, to_play: Player, max_depth: int) -> int:

    # instead of generating a board for each node in the search space,
    # have one board that gets correctly maintained with each iteration

    col_to_play = -1
    searched = 0

    def dfs(depth: int, alpha: int, beta: int) -> int:

        player = to_play if depth % 2 == 0 else to_play.opposite()

        nonlocal searched
        searched += 1

        util = utility(board)
        if util != 0:  # someone won
            return util

        if depth >= max_depth:
            return evaluate(board)

        best = None

        for x in range(board.width):
            if board.column_free(x):

                placed_x, placed_y = board.drop_column(x, player)  # places tile
                score = dfs(depth + 1, alpha, beta)
                board.set_tile(placed_x, placed_y, None)  # removes tile

                if best is None or (
                    (score > best and player.MAXXER) or
                    (score < best and player.MINNER)
                ):

                    if (  # pruning
                        (player.MAXXER and score >= beta) or
                        (player.MINNER and score <= alpha)
                    ):
                        return score

                    best = score

                    if player.MAXXER:
                        alpha = max(alpha, score)
                    else:
                        beta = min(beta, score)

                    if depth == 0:
                        nonlocal col_to_play
                        col_to_play = x

        return best

    dfs(0, float("-inf"), float("inf"))

    return col_to_play
