from pudu_ui import Controller
from pudu_ui.navigation import Navigator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app import GameApp


from constants import CREDITS
from screens import CreditsScreen


class CreditsController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app, CREDITS)
        self.app: "GameApp" = app
        self.navigator = navigator

    def on_load(self):
        super().on_load()
        self.screen = CreditsScreen(self.app.get_text)
        self.app.set_screen(self.screen)
