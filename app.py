from pudu_ui.navigation import Navigator
from pudu_ui import App


from constants import APP_NAME, LOGO, MENU, SCREEN_HEIGHT, SCREEN_WIDTH
from controllers import (
    EditNameController, LogoController, MenuController, PlayController,
    WinController
)


class GameApp(App):
    def __init__(self, is_debug: bool = False):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        self.is_debug = is_debug

        self.navigator = Navigator()

        edit_name_controller = EditNameController(self, self.navigator)
        self.navigator.add_controller(edit_name_controller)

        logo_controller = LogoController(self, self.navigator)
        self.navigator.add_controller(logo_controller)

        menu_controller = MenuController(self, self.navigator)
        self.navigator.add_controller(menu_controller)

        play_controller = PlayController(self, self.navigator)
        self.navigator.add_controller(play_controller)

        win_controller = WinController(self, self.navigator)
        self.navigator.add_controller(win_controller)

        if not self.is_debug:
            self.navigator.change(LOGO)
        else:
            self.navigator.change(MENU)

    def update(self, dt):
        controller = self.navigator.current_controller
        if (
            controller and hasattr(controller, 'update')
        ):
            controller.update(dt)
        super().update(dt)
