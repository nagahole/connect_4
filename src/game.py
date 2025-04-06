##############################################################################
# IMPORTS                                                                    #
##############################################################################

# TODO right now always plays as YELLOW

# - LIBRARIES ------------------------------------
import pygame

from pygame import draw
from typing import Iterable, Optional

# - OWN ------------------------------------------
from . import player_input

from .vec2 import Vec2
from .player_input import Input
from .gamestate import GameState

# - PORT -----------------------------------------
from .port.board import Board
from .port.player import Player


##############################################################################
# CONFIGURATIONS                                                             #
##############################################################################

# - GAME -----------------------------------------
DEFAULT_DIFFICULTY = 4  # search depth TODO customisable difficulty

BOARD_COLS = 7
BOARD_ROWS = 6

CELL_SIZE = 80
COIN_SIZE = 64

BOARD_ORIGIN = Vec2(100, 100)

# - DISPLAY --------------------------------------
SCREEN_WIDTH = BOARD_COLS * CELL_SIZE + 200
SCREEN_HEIGHT = BOARD_ROWS * CELL_SIZE + 200

# - COLORS ---------------------------------------
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FRAME_COLOUR = (128, 239, 128)
BG_COLOUR = (0, 0, 0)


##############################################################################
# STATES & VARIABLES                                                         #
##############################################################################
screen: pygame.Surface = None
clock: pygame.time.Clock = None

state: GameState = GameState(BOARD_COLS, BOARD_ROWS, Player.YELLOW, DEFAULT_DIFFICULTY)

input_action_map: dict[Input, callable] = {
    Input.LEFT: state.try_move_left,
    Input.RIGHT: state.try_move_right,
    Input.DROP: state.try_drop,
    Input.RESTART: state.try_restart
}


def init(difficulty: Optional[int]) -> None:
    global screen
    global clock

    if difficulty is None or difficulty <= 0:
        difficulty = DEFAULT_DIFFICULTY

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    state.reset(Player.YELLOW, difficulty)  # optional, since instantiation resets


def tick(events: Iterable[pygame.event.Event]) -> None:
    clock.tick(60)  # limits to 60 FPS

    pressed_keys = []

    for event in events:
        if event.type == pygame.KEYDOWN:
            pressed_keys.append(event.key)

    for inp, act in input_action_map.items():
        if inp.is_pressed(pressed_keys):
            act()


def render() -> None:
    draw_background()
    draw_frame()
    draw_coins_and_gaps()
    draw_cursor()


def draw_background() -> None:
    screen.fill(BG_COLOUR)


def draw_frame() -> None:
    size = (BOARD_COLS * CELL_SIZE, BOARD_ROWS * CELL_SIZE)  # w * h
    draw.rect(screen, FRAME_COLOUR, (*BOARD_ORIGIN, *size))


def draw_coins_and_gaps() -> None:

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):

            x = BOARD_ORIGIN.x + (col + 0.5) * CELL_SIZE
            y = BOARD_ORIGIN.y + (BOARD_ROWS - row - 0.5) * CELL_SIZE

            match state.tile_at(col, row):
                case Player.RED:
                    color = RED
                case Player.YELLOW:
                    color = YELLOW
                case _:
                    color = BG_COLOUR  # fakes "holes" with background colour

            draw.circle(screen, color, (x, y), COIN_SIZE / 2)


def draw_cursor() -> None:
    origin_x = BOARD_ORIGIN.x + (state.cursor + 0.5) * CELL_SIZE
    origin_y = BOARD_ORIGIN.y - 15

    color = YELLOW if state.playing_as == Player.YELLOW else RED

    # triangle
    SIZE = 8

    top_left = (origin_x - SIZE, origin_y - SIZE)
    top_right = (origin_x + SIZE, origin_y - SIZE)
    bottom = (origin_x, origin_y + SIZE)

    points = [top_left, top_right, bottom]

    draw.polygon(screen, color, points, 2)
