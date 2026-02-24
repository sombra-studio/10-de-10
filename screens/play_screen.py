from collections.abc import Callable
from pudu_ui import Screen


from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game
from widgets import InfoLabel, TokenList, TokenWidget
from utils import format_time


class PlayScreen(Screen):
    def __init__(
        self,
        game: Game,
        player_name: str,
        on_select_callback: Callable[[int], None] = lambda l: None
    ):
        super().__init__('PlayScreen')
        # Init UI

        # Labels
        labels_y = SCREEN_HEIGHT - 50
        time_label_x = 250
        self.time_label = InfoLabel(
            x=time_label_x, y=labels_y, text=format_time(game.time),
            batch=self.batch
        )

        name_label_x = SCREEN_WIDTH / 2
        self.name_label = InfoLabel(
            x=name_label_x, y=labels_y, text=player_name,
            batch=self.batch
        )

        count = game.get_count()
        done_label_x = SCREEN_WIDTH - time_label_x
        self.done_label = InfoLabel(
            x=done_label_x, y=labels_y, text=f"{count}/{len(game.tokens)}",
            batch=self.batch
        )

        # Tokens
        self.token_listlayout = TokenList(batch=self.batch)
        for token in game.tokens:
            token_widget = TokenWidget(
                color=token.color,
                on_select_callback=on_select_callback,
                batch=self.batch
            )
            self.token_listlayout.add(token_widget)

        self.widgets.append(self.token_listlayout)
        self.widgets.append(self.time_label)
        self.widgets.append(self.done_label)

        self.token_listlayout.focus()
