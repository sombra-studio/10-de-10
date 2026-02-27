from pudu_ui import App, Controller
from pudu_ui.navigation import Navigator


from constants import HIGHSCORES
from screens import HighscoresScreen


class HighscoresController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app, HIGHSCORES)
        self.navigator = navigator

    def on_load(self):
        super().on_load()
        self.screen = HighscoresScreen()
        self.app.set_screen(self.screen)
