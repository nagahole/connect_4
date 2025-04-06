from typing import Self
from enum import Enum


class Player(Enum):

    RED = 0
    YELLOW = 1

    @property
    def MAXXER(self) -> bool:
        return self == Player.RED

    @property
    def MINNER(self) -> bool:
        return self == Player.YELLOW

    def to_c(self) -> str:

        if self == Player.RED:
            return "r"
        else:
            return "y"

    def opposite(self) -> Self:
        if self == Player.RED:
            return Player.YELLOW

        return Player.RED

    @classmethod
    def from_str(cls: Self, s: str) -> Self:

        s = s.lower()

        if s == "red":
            return cls.RED
        elif s == "yellow":
            return cls.YELLOW
        else:
            raise RuntimeError(f"{s} string is not a valid Player type!")

    @classmethod
    def from_char(cls: Self, c: str) -> Self:

        s = s.lower()

        if s == "r":
            return cls.RED
        elif s == "y":
            return cls.YELLOW
        else:
            raise RuntimeError(f"{s} char is not a valid Player type!")
