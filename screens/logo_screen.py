from pudu_ui import Screen
from pudu_ui.image import Image, ImageParams
import pyglet


from constants import LOGO, SCREEN_WIDTH, SCREEN_HEIGHT


LOGO_WIDTH = 200
LOGO_HEIGHT = 200


class LogoScreen(Screen):
    def __init__(self):
        super().__init__(LOGO)
        image = pyglet.resource.image("logo.png")
        tex=image.get_texture()
        params = ImageParams(
            x=SCREEN_WIDTH / 2 - LOGO_WIDTH / 2,
            y=SCREEN_HEIGHT / 2 - LOGO_HEIGHT / 2,
            width=LOGO_WIDTH,
            height=LOGO_HEIGHT,
            focusable=False,
            texture=tex
        )
        self.img = Image(params=params, batch=self.batch)
