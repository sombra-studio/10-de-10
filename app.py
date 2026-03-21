import json
import os
from pudu_ui.navigation import Navigator
from pudu_ui import App
import pyglet
from pyglet.event import EVENT_HANDLED, EVENT_UNHANDLED
from pyglet.window import key


from constants import (
    APP_NAME, BELL_SOUND, DRUM_SOUND, LOGO, MENU, POP_SOUND, SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from controllers import (
    EditNameController, HighscoresController, LogoController, MenuController,
    PlayController, WinController
)
from enums import Languages
from utils import get_settings


pyglet.resource.path = ['assets/imgs', 'assets/sounds', 'locales']
pyglet.resource.reindex()


LANGUAGES_MAP = {
    Languages.EN: "en",
    Languages.ES: "es",
    Languages.FR: "fr"
}


class GameApp(App):
    def __init__(self, is_debug: bool = False):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        self.is_debug = is_debug
        self.settings = get_settings()
        self.navigator = Navigator()
        self.words = {}

        # Init language strings
        self.set_language()

        # Init sounds
        self.sounds = {
            BELL_SOUND: pyglet.resource.media("bell.wav", streaming=False),
            DRUM_SOUND: pyglet.resource.media("drum.wav", streaming=False),
            POP_SOUND: pyglet.resource.media("pop.wav", streaming=False)
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
            player.volume = self.settings.audio_volume
            return player
        return None

    def update(self, dt):
        controller = self.navigator.current_controller
        if controller and hasattr(controller, 'update'):
            controller.update(dt)
        super().update(dt)

    def on_key_press(self, symbol: int, modifiers: int):
        result = self.current_screen.on_key_press(symbol, modifiers)
        if result == EVENT_HANDLED:
            return True
        if symbol == key.ESCAPE and not (
                modifiers & ~(
                    key.MOD_NUMLOCK |
                    key.MOD_CAPSLOCK |
                    key.MOD_SCROLLLOCK
                )
        ):
            self.dispatch_event('on_close')
        return EVENT_UNHANDLED

    def set_language(self):
        folder_path = LANGUAGES_MAP[self.settings.language]
        # load locales strings
        try:
            filename = os.path.join(folder_path, "strings.json")
            with pyglet.resource.file(filename) as f:
                self.words = json.load(f)
        except FileNotFoundError:
            print(
                f"Could not find file strings.json for language "
                f"{self.settings.language}"
            )
        except json.JSONDecodeError as e:
            print(f"Error: Decoding language file {e}")

    def get_text(self, text: str):
        return self.words.get(text, "TEXT_NOT_FOUND")
