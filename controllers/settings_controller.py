from pudu_ui import Controller
from pudu_ui.navigation import Navigator


from constants import MENU, SETTINGS
from screens import SettingsScreen
from utils import write_settings


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import GameApp


class SettingsController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app, SETTINGS)
        self.app: "GameApp" = app
        self.navigator = navigator

    def on_load(self):
        self.screen = SettingsScreen(self.app.settings, self.app.get_text)
        self.app.set_screen(self.screen)
        self.screen.button.on_press = self.on_continue
        self.screen.cancel_button.on_press = self.cancel

    def on_continue(self, _):
        new_settings = self.screen.get_settings()
        self.app.settings = new_settings
        write_settings(new_settings)
        # We set the language again in case it was changed
        self.app.set_language()
        self.navigator.change(MENU)

    def cancel(self, _):
        self.navigator.change(MENU)
