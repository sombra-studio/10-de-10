from pudu_ui.layouts import ListLayout, ListLayoutParams, ListDirection
from pudu_ui import Button, ButtonParams, Screen


from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from widgets import Title


OPTIONS = ["Jugar", "Editar Nombre", "Puntajes", "Opciones", "Salir"]
GAME_TITLE = "array.sort"
MENU_WIDTH = 250
MENU_ITEM_HEIGHT = 50
INTER_ITEM_SPACING = 20
N = len(OPTIONS)
MENU_HEIGHT = int(MENU_ITEM_HEIGHT * N + INTER_ITEM_SPACING * (N - 1))



class MenuScreen(Screen):
    def __init__(self):
        super().__init__("Menu")

        # Title
        self.title = Title(text=GAME_TITLE, batch=self.batch)

        # Menu List
        params = ListLayoutParams(
            x=SCREEN_WIDTH / 2 - MENU_WIDTH / 2,
            y=SCREEN_HEIGHT / 2 - MENU_HEIGHT / 2,
            width=MENU_WIDTH, height=MENU_HEIGHT,
            inter_item_spacing=INTER_ITEM_SPACING,
            direction=ListDirection.VERTICAL
        )
        self.list_layout = ListLayout(params, batch=self.batch)

        button_params = ButtonParams()
        for option in OPTIONS:
            button_params.text = option
            new_button = Button(params=button_params, batch=self.batch)
            self.list_layout.add(new_button)

        self.widgets.append(self.list_layout)

        self.list_layout.focus()
