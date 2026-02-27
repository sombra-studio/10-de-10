from pudu_ui import Label, LabelParams
from pyglet.graphics import Batch


from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from styles.fonts import h1


TITLE_Y = SCREEN_HEIGHT - 100


class Title(Label):
    def __init__(self, text: str, batch: Batch):
        params = LabelParams(
            x=SCREEN_WIDTH / 2, y=TITLE_Y,
            anchor_x='center', anchor_y='center',
            text=text, style=h1()
        )
        super().__init__(params=params, batch=batch)
