from pudu_ui import Button, ButtonParams, Screen
from pyglet.gui import TextEntry

from constants import SCREEN_WIDTH
from widgets import CancelButton, Title

TEXT_ENTRY_WIDTH = 150
TEXT_ENTRY_HEIGHT = 32
TEXT_ENTRY_X = int(SCREEN_WIDTH / 2 - TEXT_ENTRY_WIDTH / 2)
TEXT_ENTRY_Y = 400


TITLE = "Editar Nombre"
BUTTON_X = 700
BUTTON_Y = 250
BUTTON_TEXT = "Continuar"


class EditNameScreen(Screen):
    def __init__(self, user_name: str):
        super().__init__("Edit")
        self.title = Title(text=TITLE, batch=self.batch)
        self.text_entry = TextEntry(
            text=user_name, x=TEXT_ENTRY_X, y=TEXT_ENTRY_Y, width=TEXT_ENTRY_WIDTH,
            batch=self.batch
        )
        self.text_entry.focus = True
        button_params = ButtonParams(
            x=BUTTON_X, y=BUTTON_Y,
            text=BUTTON_TEXT
        )
        self.button = Button(params=button_params, batch=self.batch)
        self.cancel_button = CancelButton(batch=self.batch)
        self.widgets.append(self.button)
