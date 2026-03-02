from pudu_ui import Screen
from pudu_ui.layouts import ListLayout, ListLayoutParams, ListDirection


from constants import SCREEN_WIDTH
from game import Score
from styles.buttons import BUTTON_HEIGHT
from widgets import BackButton, Title, ScoreRowParams, ScoreRowWidget
from widgets.buttons.cancel_button import BUTTON_Y


TITLE = "Mejores Tiempos"
LIST_WIDTH = 600
LIST_HEIGHT = 400
LIST_X = SCREEN_WIDTH / 2 - LIST_WIDTH / 2
LIST_Y = BUTTON_Y + BUTTON_HEIGHT + 20
INTER_ITEM_SPACING = 4


class HighscoresScreen(Screen):
    def __init__(self, highscores: list[Score]):
        super().__init__("Highscores")
        self.title = Title(text=TITLE, batch=self.batch)
        self.button = BackButton(batch=self.batch)
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
