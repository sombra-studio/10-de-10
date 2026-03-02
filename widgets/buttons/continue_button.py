from pudu_ui import Button, ButtonParams
from pyglet.graphics import Batch


from constants import SCREEN_WIDTH
from widgets.buttons.cancel_button import BUTTON_Y, DIST_TO_CENTER
import styles


BUTTON_X = SCREEN_WIDTH / 2 + DIST_TO_CENTER - styles.buttons.BUTTON_WIDTH / 2
BUTTON_TEXT = "Continuar"


class ContinueButton(Button):
    def __init__(self, batch: Batch):
        params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y,
            width=styles.buttons.BUTTON_WIDTH,
            height=styles.buttons.BUTTON_HEIGHT,
            text=BUTTON_TEXT
        )
        super().__init__(params=params, batch=batch)
