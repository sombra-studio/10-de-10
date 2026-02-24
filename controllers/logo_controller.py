from pudu_ui import App, Controller
from pudu_ui.colors import BLACK, WHITE
from pudu_ui.navigation import Navigator


from constants import LOGO, MENU
from screens import LogoScreen


DURATION = 3


class LogoController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app=app, name=LOGO)
        self.navigator = navigator
        self.timer = 0

    def on_load(self):
        super().on_load()
        self.app.background_color = WHITE
        self.screen = LogoScreen()
        self.app.set_screen(self.screen)

    def update(self, dt):
        self.timer += dt
        if self.timer >= DURATION:
            self.start_game()


    def start_game(self):
        self.app.background_color = BLACK
        self.navigator.change(MENU)
