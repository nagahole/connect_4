import pygame

from typing import Iterator
from numbers import Number

class Vec2(pygame.Vector2):

    def __init__(self, x: Number, y: Number):
        super()

        self.x = x
        self.y = y

    # so we can unpack - like *pos
    def __iter__(self) -> Iterator[Number]:
        yield self.x
        yield self.y
