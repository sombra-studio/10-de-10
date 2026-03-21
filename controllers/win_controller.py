from pudu_ui import Controller
from pudu_ui.navigation import Navigator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app import GameApp


from constants import MENU, WIN
from screens import WinScreen


class WinController(Controller):

    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app=app, name=WIN)
        self.app: "GameApp" = app
        self.navigator = navigator

    def on_load(self, time: float):
        super().on_load()
        self.screen = WinScreen(time, get_text=self.app.get_text)
        self.screen.button.on_press = self.on_continue
        self.app.set_screen(self.screen)

    def on_continue(self, _):
        self.navigator.change(MENU)
