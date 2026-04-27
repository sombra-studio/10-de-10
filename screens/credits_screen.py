from collections.abc import Callable
from pudu_ui import Label, LabelParams, Screen
from pudu_ui.image import Image, ImageParams
import pyglet.resource

from constants import (
    APP_VERSION, CREDITS, CREDITS_INFO_S, CREDITS_S, DEVELOPED_BY_S,
    SCREEN_WIDTH
)
from styles.fonts import p1
from widgets import ContinueButton, Title
from widgets.buttons.cancel_button import DIST_TO_CENTER


INFO_LABEL_WIDTH = 800
INFO_LABEL_HEIGHT = 250
LOGO_SIZE = 100


class CreditsScreen(Screen):
    def __init__(self, get_text: Callable[str, str]):
        super().__init__(CREDITS)
        self.title = Title(get_text(CREDITS_S), self.batch)
        programmer = "Jesús Henríquez"
        credits_info = get_text(CREDITS_INFO_S).format(programmer, APP_VERSION)
        self.info_label = Label(
            LabelParams(
                width=INFO_LABEL_WIDTH, height=INFO_LABEL_HEIGHT,
                anchor_y='bottom',
                text=credits_info, multiline=True, style=p1()
            ), batch=self.batch
        )
        self.info_label.x = SCREEN_WIDTH / 2 - self.info_label.width / 2
        self.info_label.y = self.title.y - 100 - self.info_label.height
        self.info_label.invalidate()

        self.button = ContinueButton(self.batch, get_text)
        self.button.x -= DIST_TO_CENTER
        self.button.invalidate()

        logo_tex = pyglet.resource.image('logo.png').get_texture()
        logo_y = self.button.y + 100
        logo_params = ImageParams(
            x=SCREEN_WIDTH / 2 - LOGO_SIZE / 2, y=logo_y,
            width=LOGO_SIZE, height=LOGO_SIZE, texture=logo_tex
        )
        self.developer_logo = Image(params=logo_params, batch=self.batch)

        self.developer_label = Label(
            LabelParams(
                x=SCREEN_WIDTH / 2.0, y=self.developer_logo.y + LOGO_SIZE + 50,
                text=get_text(DEVELOPED_BY_S),
                anchor_x='center', anchor_y='center', style=p1()
            ), batch=self.batch
        )

        self.widgets.append(self.developer_logo)
        self.widgets.append(self.developer_label)
        self.widgets.append(self.info_label)
        self.widgets.append(self.button)
