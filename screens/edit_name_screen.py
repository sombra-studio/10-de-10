from pudu_ui import Screen
from pyglet.gui import TextEntry

from constants import SCREEN_WIDTH


TEXT_ENTRY_WIDTH = 150
TEXT_ENTRY_HEIGHT = 32
TEXT_ENTRY_X = int(SCREEN_WIDTH / 2 - TEXT_ENTRY_WIDTH / 2)
TEXT_ENTRY_Y = 400


class EditNameScreen(Screen):
    def __init__(self, user_name: str):
        super().__init__("Edit")
        self.text_entry = TextEntry(
            text=user_name, x=TEXT_ENTRY_X, y=TEXT_ENTRY_Y, width=TEXT_ENTRY_WIDTH,
            batch=self.batch
        )
        self.text_entry.focus = True
