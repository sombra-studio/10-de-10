from collections.abc import Callable
from pudu_ui import Button, ButtonParams, Screen
from pudu_ui.layouts import ListLayout, ListLayoutParams, ListDirection


from constants import BEST_TIMES_S, GO_TO_MENU_S, SCREEN_WIDTH
from game import Score
import styles
from styles.buttons import BUTTON_HEIGHT
from widgets import Title, ScoreRowParams, ScoreRowWidget
from widgets.buttons.cancel_button import BUTTON_Y


LIST_WIDTH = 600
LIST_HEIGHT = 400
LIST_X = SCREEN_WIDTH / 2 - LIST_WIDTH / 2
LIST_Y = BUTTON_Y + BUTTON_HEIGHT + 20
INTER_ITEM_SPACING = 4


class HighscoresScreen(Screen):
    def __init__(self, highscores: list[Score], get_text: Callable[str, str]):
        super().__init__("Highscores")
        self.title = Title(text=get_text(BEST_TIMES_S), batch=self.batch)

        btn_width = styles.buttons.BUTTON_WIDTH
        button_params = ButtonParams(
            x=SCREEN_WIDTH / 2 - btn_width / 2, y=BUTTON_Y,
            width=btn_width
        )
        self.button = Button(params=button_params, batch=self.batch)
        self.button.text = get_text(GO_TO_MENU_S)
        self.button.invalidate()

        layout_params = ListLayoutParams(
            x=LIST_X, y=LIST_Y, width=LIST_WIDTH, height=LIST_HEIGHT,
            inter_item_spacing=INTER_ITEM_SPACING, resizes_item_height=False,
            direction=ListDirection.VERTICAL
        )
        layout = ListLayout(layout_params, batch=self.batch)

        for i, score in enumerate(highscores):
            params = ScoreRowParams(
                position=(i + 1), player_name=score.player_name, time=score.time
            )
            new_row = ScoreRowWidget(params=params, batch=self.batch)
            layout.add(new_row)

        self.widgets.append(self.button)
        self.widgets.append(layout)
