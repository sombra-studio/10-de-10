from pudu_ui import Controller
from pudu_ui.navigation import Navigator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app import GameApp


from constants import HIGHSCORES, MENU
from screens import HighscoresScreen
from utils import get_highscores


class HighscoresController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app, HIGHSCORES)
        self.app: "GameApp" = app
        self.navigator = navigator

    def on_load(self):
        super().on_load()
        highscores = get_highscores()
        self.screen = HighscoresScreen(highscores, get_text=self.app.get_text)
        self.app.set_screen(self.screen)
        self.screen.button.on_press = lambda l: self.navigator.change(MENU)
