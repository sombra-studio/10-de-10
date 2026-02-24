from pudu_ui import Button, Label, LabelParams, Screen
from pudu_ui.styles.fonts import h1, h2


from constants import FONT_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from utils import format_time


class WinScreen(Screen):
    def __init__(self, time: float):
        super().__init__("Win")
        win_label_style = h1()
        win_label_style.color = FONT_COLOR
        win_label_y = 3 * SCREEN_HEIGHT / 4
        win_label_params = LabelParams(
            x=SCREEN_WIDTH/2, y=win_label_y,
            text="GANASTE!", anchor_x='center', anchor_y='center',
            style=win_label_style
        )
        self.win_label = Label(win_label_params, batch=self.batch)

        time_label_style = h2()
        time_text = f"Tu tiempo fue {format_time(time)}"
        time_label_params = LabelParams(
            x=SCREEN_WIDTH / 2, y=3 * SCREEN_HEIGHT / 4,
            text=time_text, anchor_x='center', anchor_y='center',
            style=time_label_style
        )
        self.time_label = Label(time_label_params, batch=self.batch)

        self.button = Button(batch=self.batch)

        self.widgets.append(self.button)
