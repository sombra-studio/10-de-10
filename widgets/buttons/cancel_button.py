from collections.abc import Callable
from pudu_ui import ButtonParams
from pyglet.graphics import Batch


from constants import CANCEL_S, SCREEN_WIDTH
import styles
from widgets.buttons import SecondaryButton


DIST_TO_CENTER = 120
BUTTON_X = SCREEN_WIDTH / 2 - DIST_TO_CENTER - styles.buttons.BUTTON_WIDTH / 2
BUTTON_Y = 80


class CancelButton(SecondaryButton):
    def __init__(self, batch: Batch, get_text: Callable[str, str]):
        params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y,
            width=styles.buttons.BUTTON_WIDTH,
            height=styles.buttons.BUTTON_HEIGHT,
            text=get_text(CANCEL_S)
        )
        super().__init__(params=params, batch=batch)
