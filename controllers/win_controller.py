from pudu_ui import App, Controller
from pudu_ui.navigation import Navigator


from constants import MENU, WIN
from screens import WinScreen


class WinController(Controller):

    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app=app, name=WIN)
        self.navigator = navigator

    def on_load(self, time: float):
        super().on_load()
        self.screen = WinScreen(time)
        self.screen.button.on_press = self.on_continue
        self.app.set_screen(self.screen)

    def on_continue(self, _):
        self.navigator.change(MENU)
