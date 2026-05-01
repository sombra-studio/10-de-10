from collections.abc import Callable

from pudu_ui import Button, ButtonParams
from pyglet.graphics import Batch


from constants import CONTINUE_S, SCREEN_WIDTH
from widgets.buttons.cancel_button import BUTTON_Y, DIST_TO_CENTER
import styles


BUTTON_X = SCREEN_WIDTH / 2 + DIST_TO_CENTER - styles.buttons.BUTTON_WIDTH / 2


class ContinueButton(Button):
    def __init__(self, batch: Batch, get_text: Callable[[str], str]):
        params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y,
            width=styles.buttons.BUTTON_WIDTH,
            height=styles.buttons.BUTTON_HEIGHT,
            text=get_text(CONTINUE_S)
        )
        super().__init__(params=params, batch=batch)
