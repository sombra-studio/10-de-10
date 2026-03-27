from pudu_ui import Controller
from pudu_ui.navigation import Navigator
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import GameApp

from constants import (
    BELL_SOUND, DRUM_SOUND, MAX_SCORES_COUNT, MENU, PLAY, POP_SOUND,
    WIN
)
from game import Game, Score, get_random_tokens
from screens import PlayScreen
from utils import format_time, get_highscores, write_highscores


SWAP_ANIMATION_TIME = 0.4


class PlayController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        self.selected_token_idx = None
        self.game = None
        self.user_name = ""
        super().__init__(app=app, name=PLAY)
        self.app: "GameApp" = app
        self.navigator = navigator
        self.previous_count = 0
        self.is_on_pause = False

    def on_load(self, user_name: str):
        super().on_load()
        self.user_name = user_name

        # Init Game
        tokens = get_random_tokens()
        original_tokens = get_random_tokens()
        start_time = 0.0

        self.game = Game(tokens, original_tokens, start_time, user_name)
        self.previous_count = self.game.get_count()
        if self.game.is_solved():
            # ensure game is not solved
            self.game.swap(0, 9)
        self.is_on_pause = False

        self.screen = PlayScreen(
            game=self.game,
            player_name=user_name,
            get_text=self.app.get_text,
            on_select_callback=self.on_select_token,
            on_go_to_menu_callback=self.go_to_menu,
            on_pause_callback=self.pause_game,
            on_unpause_callback=self.on_unpause_callback
        )
        self.app.set_screen(self.screen)

    def update(self, dt: float):
        if self.is_on_pause:
            return

        if self.game.is_solved():
            self.won()
            return

        self.game.time += dt
        self.screen.time_label.text = format_time(self.game.time)
        self.screen.time_label.invalidate()

    def go_to_menu(self, *_):
        self.navigator.change(MENU, self.user_name)

    def pause_game(self, *_):
        self.is_on_pause = True
        self.screen.is_on_pause = True
        self.screen.popup.open()
        self.screen.token_listlayout.is_focusable = False

    def on_select_token(self, idx: int):
        n = len(self.game.tokens)
        if not (0 <= idx < n):
            return

        if self.selected_token_idx is not None:
            if self.selected_token_idx == idx:
                # If we select a token again we want to unselect them
                self.selected_token_idx = None
                return

            # Here we have a previously selected token and a new token

            # Swap tokens
            i = self.selected_token_idx
            j = idx
            self.game.swap(i, j)

            token_widgets = self.screen.token_listlayout.children
            token_widgets[i].unselect()
            token_widgets[j].unselect()
            temp = token_widgets[i]
            token_widgets[i] = token_widgets[j]
            token_widgets[j] = temp

            self.screen.token_listlayout.invalidate()
            if self.screen.token_listlayout.is_on_focus:
                self.screen.token_listlayout.get_current_item().focus()
            self.selected_token_idx = None

            # Recompute the list for the new positions
            self.screen.token_listlayout.recompute()

            # Animate tokens
            x_i, y_i = token_widgets[i].x, token_widgets[i].y
            x_j, y_j = token_widgets[j].x, token_widgets[j].y
            token_widgets[i].lerp_from_position(x_j, y_j, SWAP_ANIMATION_TIME)
            token_widgets[j].lerp_from_position(x_i, y_i, SWAP_ANIMATION_TIME)

            # Check new score
            score = self.game.get_count()
            if score > self.previous_count:
                self.app.play_sound(BELL_SOUND)
            elif score < self.previous_count:
                self.app.play_sound(DRUM_SOUND)
            self.previous_count = score

            total = len(self.game.tokens)
            # There could be a better way of updating UI from changes in the
            # model, for now it's all manual
            self.screen.done_label.text = f"{score}/{total}"
            self.screen.done_label.invalidate()

            self.app.play_sound(POP_SOUND)
        else:
            # Store currently selected token
            self.selected_token_idx = idx

    def on_unpause_callback(self, *_):
        self.is_on_pause = False
        self.screen.is_on_pause = False
        self.screen.popup.dismiss()
        self.screen.token_listlayout.is_focusable = True

    def won(self):
        # Get the highscores
        highscores = get_highscores()

        # Check if new score should be added to highscores
        score_added = False
        for i, score in enumerate(highscores):
            # We assume highscores come in ascending order
            if self.game.time < score.time:
                new_score = Score(self.user_name, self.game.time)
                highscores.insert(i, new_score)
                score_added = True
                break

        if len(highscores) < MAX_SCORES_COUNT and not score_added:
            new_score = Score(self.user_name, self.game.time)
            highscores.append(new_score)
            score_added = True

        if score_added:
            # Write the highscores again
            write_highscores(highscores)

        # Change to the win screen
        self.navigator.change(WIN, self.game.time)
