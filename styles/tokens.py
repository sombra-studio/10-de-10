from dataclasses import dataclass, field
from pudu_ui import Color
from pudu_ui.colors import WHITE, GRAY


def default_border_color() -> Color:
    return WHITE


def default_token_color() -> Color:
    return GRAY


@dataclass
class TokenStyle:
    color: Color = field(default_factory=default_token_color)
    border_width: int = 0
    border_color: Color = field(default_factory=default_border_color)
