import pygame

from enum import Enum
from typing import Iterable


class Input(Enum):
    LEFT = frozenset([pygame.K_a, pygame.K_LEFT])
    RIGHT = frozenset([pygame.K_d, pygame.K_RIGHT])
    DROP = frozenset([pygame.K_s, pygame.K_KP_ENTER, pygame.K_SPACE])
    RESTART = frozenset([pygame.K_r])

    def is_pressed(self, pressed_keys: Iterable[int]) -> bool:
        return any(k in self.value for k in pressed_keys)

