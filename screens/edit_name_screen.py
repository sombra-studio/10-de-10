from pudu_ui import Screen
from pyglet.gui import TextEntry
from collections.abc import Callable


from constants import CANCEL_S, CONTINUE_S, EDIT_NAME_S, SCREEN_WIDTH
from widgets import CancelButton, ContinueButton, Title


TEXT_ENTRY_WIDTH = 150
TEXT_ENTRY_HEIGHT = 32
TEXT_ENTRY_X = int(SCREEN_WIDTH / 2 - TEXT_ENTRY_WIDTH / 2)
TEXT_ENTRY_Y = 400


class EditNameScreen(Screen):
    def __init__(self, user_name: str, get_text: Callable[str, str]):
        super().__init__("Edit")
        self.title = Title(text=get_text(EDIT_NAME_S), batch=self.batch)
        self.text_entry = TextEntry(
            text=user_name, x=TEXT_ENTRY_X, y=TEXT_ENTRY_Y, width=TEXT_ENTRY_WIDTH,
            batch=self.batch
        )

        self.text_entry.focus = True
        self.button = ContinueButton(batch=self.batch)
        self.button.text = get_text(CONTINUE_S)
        self.button.invalidate()

        self.cancel_button = CancelButton(batch=self.batch)
        self.cancel_button.text = get_text(CANCEL_S)
        self.cancel_button.invalidate()

        self.widgets.append(self.button)
        self.widgets.append(self.cancel_button)
