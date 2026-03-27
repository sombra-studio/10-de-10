import pudu_ui
from pyglet.enums import Weight


FONT_COLOR =  pudu_ui.colors.WHITE


def h1():
    style = pudu_ui.styles.fonts.h1()
    style.color = FONT_COLOR
    return style


def h2():
    style = pudu_ui.styles.fonts.h2()
    style.color = FONT_COLOR
    return style


def p1():
    style = pudu_ui.styles.fonts.p1()
    style.color = FONT_COLOR
    return style


def b1():
    style = p1()
    style.weight = Weight.BOLD
    return style
