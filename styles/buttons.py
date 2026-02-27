from pudu_ui.colors import *
from pudu_ui.styles.buttons import (
    ButtonStyle, DEFAULT_BTN_BORDER_WIDTH, DEFAULT_BTN_CORNER_RADIUS
)
from pudu_ui.styles.frames import FrameStyle


from styles.fonts import p1


BUTTON_WIDTH = 150
BUTTON_HEIGHT = 70
BTN_HOVER_BG_COLOR = GRAY
BTN_FOCUS_FONT_COLOR = LIGHTER_GRAY
BTN_PRESS_BG_COLOR = DARKER_GRAY
BTN_PRESS_FONT_COLOR = GRAY


def secondary_btn_style() -> ButtonStyle:
    frame_style = FrameStyle(
        start_color=DARK_GRAY
    )
    frame_style.set_uniform_radius(DEFAULT_BTN_CORNER_RADIUS)

    font_style = p1()
    font_style.color = LIGHT_GRAY

    style = ButtonStyle()
    style.frame_style = frame_style
    style.font_style = font_style

    return style


def secondary_btn_hover_style() -> ButtonStyle:
    style = secondary_btn_style()
    style.frame_style.start_color = BTN_HOVER_BG_COLOR
    style.font_style.color = BTN_FOCUS_FONT_COLOR
    return style


def secondary_btn_focus_style() -> ButtonStyle:
    style = secondary_btn_style()
    style.frame_style.border_width = DEFAULT_BTN_BORDER_WIDTH
    style.font_style.color = BTN_FOCUS_FONT_COLOR
    return style


def secondary_btn_press_style() -> ButtonStyle:
    style = secondary_btn_style()
    style.frame_style.start_color = BTN_PRESS_BG_COLOR
    style.font_style.color = BTN_PRESS_FONT_COLOR
    return style
