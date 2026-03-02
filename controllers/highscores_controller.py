from pudu_ui import App, Controller
from pudu_ui.navigation import Navigator


from constants import HIGHSCORES, MENU
from screens import HighscoresScreen
from utils import get_highscores


class HighscoresController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app, HIGHSCORES)
        self.navigator = navigator

    def on_load(self):
        super().on_load()
        highscores = get_highscores()
        self.screen = HighscoresScreen(highscores)
        self.app.set_screen(self.screen)
        self.screen.button.on_press = lambda l: self.navigator.change(MENU)
