from collections.abc import Callable
from pudu_ui import Screen

from constants import CREDITS



class CreditsScreen(Screen):
    def __init__(self, get_text: Callable[str, str]):
        super().__init__(CREDITS)

