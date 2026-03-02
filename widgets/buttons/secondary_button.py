from pudu_ui import Button, ButtonParams
from pyglet.graphics import Batch


import styles


class SecondaryButton(Button):
    def __init__(self, params: ButtonParams, batch: Batch):
        params.style = styles.buttons.secondary_btn_style()
        params.hover_style = styles.buttons.secondary_btn_hover_style()
        params.focus_style = styles.buttons.secondary_btn_focus_style()
        params.press_style = styles.buttons.secondary_btn_press_style()
        super().__init__(params=params, batch=batch)
