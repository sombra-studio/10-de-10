from pudu_ui import Controller
from pudu_ui.navigation import Navigator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app import GameApp
from constants import EDIT_NAME, MENU
from screens import EditNameScreen
from utils import write_user_name


class EditNameController(Controller):
    def __init__(self, app: "GameApp", navigator: Navigator):
        super().__init__(app=app, name=EDIT_NAME)
        self.app: "GameApp" = app
        self.navigator = navigator
        self.user_name = ""

    def on_load(self, user_name: str):
        super().on_load()
        self.user_name = user_name
        self.screen = EditNameScreen(
            user_name=user_name, get_text=self.app.get_text
        )
        self.screen.text_entry.set_handler('on_commit', self.on_commit)
        self.app.set_screen(self.screen)
        self.app.push_handlers(self.screen.text_entry)
        self.screen.button.on_press = self.on_commit
        self.screen.cancel_button.on_press = self.cancel

    def on_commit(self, *_):
        text = self.screen.text_entry.value
        write_user_name(text)
        self.user_name = text
        # how can we pass new data from the controller to the app?
        # In this case the new user name. One way is just passing it from
        # screen to screen, MENU -> PLAY
        self.navigator.change(MENU, user_name=text)

    def cancel(self, _):
        self.navigator.change(MENU, user_name=self.user_name)

    def on_close(self):
        super().on_close()
        self.app.pop_handlers() # Remove the handler for text entry
