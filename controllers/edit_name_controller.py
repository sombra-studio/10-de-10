from pudu_ui import App, Controller
from pudu_ui.navigation import Navigator


from constants import EDIT_NAME, MENU
from screens import EditNameScreen


class EditNameController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app=app, name=EDIT_NAME)
        self.navigator = navigator

    def on_load(self):
        super().on_load()
        self.screen = EditNameScreen()
        self.screen.text_entry.set_handler('on_commit', self.on_commit)
        self.screen.text_entry.focus = True
        self.app.set_screen(self.screen)
        self.app.push_handlers(self.screen.text_entry)

    def on_commit(self, _, text: str):
        print(f"new name {text}")
        self.navigator.change(MENU)

    def on_close(self):
        super().on_close()
        self.app.pop_handlers() # Remove the handler for text entry
