from pudu_ui.colors import WHITE
from pudu_ui.layouts import ListLayout, ListLayoutParams, ListDirection
from pudu_ui.styles.fonts import h1
from pudu_ui import Button, ButtonParams, Label, LabelParams, Screen


from constants import SCREEN_WIDTH, SCREEN_HEIGHT


OPTIONS = ["Jugar", "Editar Nombre", "Puntajes", "Opciones", "Salir"]
GAME_TITLE = "array.sort"
TITLE_Y = SCREEN_HEIGHT - 100
MENU_WIDTH = 250
MENU_ITEM_HEIGHT = 50
INTER_ITEM_SPACING = 20
N = len(OPTIONS)
MENU_HEIGHT = int(MENU_ITEM_HEIGHT * N + INTER_ITEM_SPACING * (N - 1))



class MenuScreen(Screen):
    def __init__(self):
        super().__init__("Menu")

        # Title
        label_style = h1()
        label_style.color = WHITE
        label_params = LabelParams(
            x=SCREEN_WIDTH / 2, y=TITLE_Y,
            anchor_x='center', anchor_y='center',
            text=GAME_TITLE, style=label_style
        )
        self.title_label = Label(params=label_params, batch=self.batch)

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
