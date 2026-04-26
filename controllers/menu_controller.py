from pudu_ui.navigation import Navigator
from pudu_ui import Button, Controller
import pyglet.app
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app import GameApp


from constants import CREDITS, EDIT_NAME, HIGHSCORES, MENU, PLAY, SETTINGS
from screens import MenuScreen
from utils import get_user_name


class MenuController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app=app, name=MENU)
        self.app: "GameApp" = app
        self.navigator = navigator
        self.button_maps = [
            self.play,
            self.edit_name,
            self.scores,
            self.settings,
            self.credits,
            self.exit
        ]
        self.user_name = ""
        self.highscores = []

    def on_load(self, user_name: str = ""):
        super().on_load()
        if not user_name:
            user_name = get_user_name()
        self.user_name = user_name

        # Load screen
        self.screen = MenuScreen(get_text=self.app.get_text)
        self.app.set_screen(self.screen)

        # Set on press for buttons
        for button in self.screen.list_layout.children:
            button.on_press = self.handle_on_press

    def handle_on_press(self, button_pressed: Button):
        self.button_maps[button_pressed.index]()

    def play(self):
        self.navigator.change(PLAY, user_name=self.user_name)

    def edit_name(self):
        self.navigator.change(EDIT_NAME, user_name=self.user_name)

    def scores(self):
        self.navigator.change(HIGHSCORES)

    def settings(self):
        self.navigator.change(SETTINGS)

    def credits(self):
        self.navigator.change(CREDITS)

    def exit(self):
        self.close()
        pyglet.app.exit()
