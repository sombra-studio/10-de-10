import json
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
    CreditsController, EditNameController, HighscoresController, LogoController,
    MenuController,
    PlayController, SettingsController, WinController
)
from utils import get_settings


pyglet.options.dpi_scaling = 'platform'
pyglet.resource.path += ['./assets', './locales']
pyglet.resource.reindex()


class GameApp(App):
    def __init__(self, is_debug: bool = False):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        app_logo = pyglet.resource.image("imgs/line-game-logo.png")
        self.set_icon(app_logo)
        self.is_debug = is_debug
        self.settings = get_settings()
        self.navigator = Navigator()
        self.words = {}

        # Init language strings
        self.set_language()

        # Init sounds
        self.sounds = {
            BELL_SOUND: pyglet.resource.audio(
                "sounds/bell.wav", streaming=False
            ),
            DRUM_SOUND: pyglet.resource.audio(
                "sounds/drum.wav", streaming=False
            ),
            POP_SOUND: pyglet.resource.audio(
                "sounds/pop.wav", streaming=False
            )
        }

        # Initialize controllers
        credits_controller = CreditsController(self, self.navigator)
        self.navigator.add_controller(credits_controller)

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

        settings_controller = SettingsController(self, self.navigator)
        self.navigator.add_controller(settings_controller)

        win_controller = WinController(self, self.navigator)
        self.navigator.add_controller(win_controller)

        # Start navigation
        if not self.is_debug:
            self.navigator.change(LOGO)
        else:
            self.navigator.change(MENU)

    def play_sound(self, sound_name: str) -> pyglet.media.AudioPlayer | None:
        if self.settings.muted:
            # Ignore this method if muted
            return None

        if sound_name in self.sounds:
            player = self.sounds[sound_name].play()
            player.volume = self.settings.audio_volume / 100.0
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
        if modifiers & key.MOD_CTRL and symbol == key.S:
            pyglet.graphics.framebuffer.get_screenshot().save("screenshot.png")

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
        folder_path = self.settings.language.name.lower()
        # load locales strings
        filename = f"{folder_path}/strings.json"
        with pyglet.resource.file(filename) as f:
            try:
                self.words = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error: Decoding language file {e}")

    def get_text(self, text: str):
        return self.words.get(text, "TEXT_NOT_FOUND")


