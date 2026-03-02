from pudu_ui import ButtonParams
from pyglet.graphics import Batch

from constants import SCREEN_WIDTH
from widgets.buttons import SecondaryButton
from widgets.buttons.cancel_button import BUTTON_Y

BTN_WIDTH = 120
BTN_HEIGHT = 74
BTN_X = SCREEN_WIDTH / 2 - BTN_WIDTH / 2
BUTTON_TEXT = "Volver"


class BackButton(SecondaryButton):
    def __init__(
        self, params: ButtonParams | None = None,
        batch: Batch | None = None
    ):
        if not params:
            params = ButtonParams(
                x=BTN_X, y=BUTTON_Y, width=BTN_WIDTH, height=BTN_HEIGHT,
                text=BUTTON_TEXT
            )
        super().__init__(params=params, batch=batch)
