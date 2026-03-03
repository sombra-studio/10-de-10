from pudu_ui.navigation import Navigator
from pudu_ui import App
import pyglet

from constants import (
    APP_NAME, BELL_SOUND, DRUM_SOUND, LOGO, MENU, POP_SOUND, SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from controllers import (
    EditNameController, HighscoresController, LogoController, MenuController,
    PlayController, WinController
)


class GameApp(App):
    def __init__(self, is_debug: bool = False):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        self.is_debug = is_debug
        self.volume = 0.3
        self.navigator = Navigator()

        # Init sounds
        pyglet.resource.path = ['assets/imgs', 'assets/sounds']
        self.sounds = {
            BELL_SOUND: pyglet.resource.media(
                "bell.mp3", streaming=False
            ),
            DRUM_SOUND: pyglet.resource.media(
                "drum.mp3", streaming=False
            ),
            POP_SOUND: pyglet.resource.media(
                "pop.mp3", streaming=False
            )
        }

        # Initialize controllers
        edit_name_controller = EditNameController(self, self.navigator)
        self.navigator.add_controller(edit_name_controller)

        highscores_controller = HighscoresController(self, self.navigator)
        self.navigator.add_controller(highscores_controller)

        logo_controller = LogoController(self, self.navigator)
        self.navigator.add_controller(logo_controller)

        menu_controller = MenuController(self, self.navigator)
        self.navigator.add_controller(menu_controller)

        play_controller = PlayController(self, self.navigator)
        self.navigator.add_controller(play_controller)

        win_controller = WinController(self, self.navigator)
        self.navigator.add_controller(win_controller)

        # Start navigation
        if not self.is_debug:
            self.navigator.change(LOGO)
        else:
            self.navigator.change(MENU)

    def play_sound(self, sound_name: str) -> pyglet.media.Player | None:
        if sound_name in self.sounds:
            player = self.sounds[sound_name].play()
            player.volume = self.volume
            return player
        return None


    def update(self, dt):
        controller = self.navigator.current_controller
        if controller and hasattr(controller, 'update'):
            controller.update(dt)
        super().update(dt)
