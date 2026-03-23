from pudu_ui import Controller
from pudu_ui.navigation import Navigator


from typing import TYPE_CHECKING

from screens import SettingsScreen

if TYPE_CHECKING:
    from app import GameApp


from constants import SETTINGS


class SettingsController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app, SETTINGS)
        self.app: "GameApp" = app
        self.navigator = navigator

    def on_load(self):
        self.screen = SettingsScreen(self.app.settings, self.app.get_text)
        self.app.set_screen(self.screen)
