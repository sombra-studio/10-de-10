from collections.abc import Callable
from typing import Any

from pudu_ui import Screen, PopUpParams, PopUp
from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.window import key

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game
from widgets import InfoLabel, TokenList, TokenWidget
from utils import format_time


POPUP_WIDTH = 400
POPUP_HEIGHT = 190


class PlayScreen(Screen):
    def __init__(
        self,
        game: Game,
        player_name: str,
        on_select_callback: Callable[[int], None] = lambda l: None,
        on_go_to_menu_callback: Callable[Any, None] = lambda l: None,
        on_pause_callback: Callable[Any, None] = lambda l: None,
        on_unpause_callback: Callable[Any, None] = lambda l: None
    ):
        super().__init__('PlayScreen')
        self.is_ready = False
        self.is_on_pause = False
        self.on_pause_callback = on_pause_callback
        self.on_unpause_callback = on_unpause_callback

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

        # Pause popup
        popup_params = PopUpParams(
            x=SCREEN_WIDTH // 2 - POPUP_WIDTH // 2,
            y=SCREEN_HEIGHT // 2 - POPUP_HEIGHT // 2,
            width=POPUP_WIDTH,
            height=POPUP_HEIGHT,
            title="Pausa",
            opt1_text="Volver al juego",
            opt1_callback=on_unpause_callback,
            opt2_text="Ir al menu",
            opt2_callback=on_go_to_menu_callback
        )
        self.popup = PopUp(params=popup_params, batch=self.batch)

        self.widgets.append(self.token_listlayout)
        self.widgets.append(self.time_label)
        self.widgets.append(self.done_label)
        self.widgets.append(self.popup)

        self.token_listlayout.focus()
    
    def update(self, dt):
        if not self.is_ready:
            super().update(dt)
            self.is_ready = True
        super().update(dt)

    def draw(self):
        if self.is_ready:
            super().draw()

    def on_key_press(self, symbol, _) -> EVENT_HANDLE_STATE:
        result = super().on_key_press(symbol, _)
        if result == EVENT_HANDLED:
            return True

        if symbol == key.ESCAPE:
            if self.is_on_pause:
                self.on_unpause_callback()
            else:
                self.on_pause_callback()
            return True
        return EVENT_UNHANDLED