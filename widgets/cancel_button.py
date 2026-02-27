from pudu_ui import Button, ButtonParams
from pyglet.graphics import Batch


BUTTON_X = 450
BUTTON_Y = 250


class CancelButton(Button):
    def __init__(self, batch: Batch):
        params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y, width=150, height=80,
        )
        super().__init__(params=params, batch=batch)
