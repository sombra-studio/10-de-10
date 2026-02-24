from pudu_ui.navigation import Navigator
from pudu_ui import App, Button, Controller
import pyglet.app

from constants import EDIT_NAME, MENU, PLAY
from screens import MenuScreen


class MenuController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app=app, name=MENU)
        self.navigator = navigator
        self.button_maps = [
            self.play,
            self.edit_name,
            self.scores,
            self.settings,
            self.exit
        ]

    def on_load(self):
        super().on_load()
        # Load screen
        self.screen = MenuScreen()
        self.app.set_screen(self.screen)

        # Set on press for buttons
        for button in self.screen.list_layout.children:
            button.on_press = self.handle_on_press

    def handle_on_press(self, button_pressed: Button):
        self.button_maps[button_pressed.index]()

    def play(self):
        self.navigator.change(PLAY)

    def edit_name(self):
        self.navigator.change(EDIT_NAME)

    def scores(self):
        pass

    def settings(self):
        pass

    def exit(self):
        self.close()
        pyglet.app.exit()

    def update(self, dt: float):
        pass
