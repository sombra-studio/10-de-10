from dataclasses import dataclass
from pudu_ui.colors import (
    Color,
    GRAY, ORANGE, RED, YELLOW, GREEN, BLUE_GREEN, BLUE, PURPLE, VIOLET, MAROON
)
import random


NUM_TOKENS = 10


@dataclass
class Score:
    player_name: str = "default name"
    time: float = 1000


@dataclass
class Token:
    color: Color

    def __eq__(self, other) -> bool:
        if isinstance(other, Token):
            return self.color.as_tuple() == other.color.as_tuple()
        return False



@dataclass
class Game:
    tokens: list[Token]
    original_tokens: list[Token]
    time: float
    player_name: str

    def get_count(self):
        count = 0
        n = len(self.tokens)
        for i in range(n):
            if self.tokens[i].color == self.original_tokens[i].color:
                count += 1
        return count

    def is_solved(self):
        n = len(self.tokens)
        for i in range(n):
            if self.tokens[i].color != self.original_tokens[i].color:
                return False
        return True

    def swap(self, i: int, j: int):
        temp = self.tokens[i]
        self.tokens[i] = self.tokens[j]
        self.tokens[j] = temp


def get_colors() -> list[Color]:
    return [
        ORANGE, RED, YELLOW, GREEN, BLUE_GREEN, BLUE, PURPLE, VIOLET, MAROON,
        GRAY
    ]


def get_random_tokens() -> list[Token]:
    colors = get_colors()
    tokens = [Token(color) for color in colors]
    random.shuffle(tokens)
    return tokens
