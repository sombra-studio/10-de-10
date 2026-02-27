from pudu_ui import Button, ButtonParams
from pyglet.graphics import Batch


from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import styles


DIST_TO_CENTER = 120
BUTTON_X = SCREEN_WIDTH / 2 - DIST_TO_CENTER - styles.buttons.BUTTON_WIDTH / 2
BUTTON_Y = SCREEN_HEIGHT / 4
BUTTON_TEXT = "Cancelar"


class CancelButton(Button):
    def __init__(self, batch: Batch):
        style = styles.buttons.secondary_btn_style()
        hover_style = styles.buttons.secondary_btn_hover_style()
        focus_style = styles.buttons.secondary_btn_focus_style()
        press_style = styles.buttons.secondary_btn_press_style()
        params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y,
            width=styles.buttons.BUTTON_WIDTH,
            height=styles.buttons.BUTTON_HEIGHT,
            text=BUTTON_TEXT,
            style=style,
            hover_style=hover_style,
            focus_style=focus_style,
            press_style=press_style
        )
        super().__init__(params=params, batch=batch)
