from collections.abc import Callable

from pudu_ui import Button, ButtonParams, Label, LabelParams, Screen

from constants import (
    CONTINUE_S, SCREEN_WIDTH, SCREEN_HEIGHT, YOUR_TIME_S,
    YOU_WIN_S
)
import styles.buttons
from styles.fonts import h1, h2
from utils import format_time


TIME_LABEL_MARGIN_Y = 50
BUTTON_Y = 200


class WinScreen(Screen):
    def __init__(self, time: float, get_text: Callable[str, str]):
        super().__init__("Win")
        win_label_style = h1()
        win_label_y = 3 * SCREEN_HEIGHT / 4
        win_label_params = LabelParams(
            x=SCREEN_WIDTH/2, y=win_label_y,
            text=get_text(YOU_WIN_S), anchor_x='center', anchor_y='center',
            style=win_label_style
        )
        self.win_label = Label(win_label_params, batch=self.batch)

        time_label_style = h2()
        time_text = get_text(YOUR_TIME_S) + f"{format_time(time)}"
        time_label_y = win_label_y - TIME_LABEL_MARGIN_Y
        time_label_params = LabelParams(
            x=SCREEN_WIDTH / 2, y=time_label_y,
            text=time_text, anchor_x='center', anchor_y='center',
            style=time_label_style
        )
        self.time_label = Label(time_label_params, batch=self.batch)

        btn_width = styles.buttons.BUTTON_WIDTH
        button_params = ButtonParams(
            x=SCREEN_WIDTH / 2 - btn_width / 2, y=BUTTON_Y,
            width=btn_width
        )
        self.button = Button(params=button_params, batch=self.batch)
        self.button.text = get_text(CONTINUE_S)
        self.button.invalidate()
        self.button.focus()

        self.widgets.append(self.button)
