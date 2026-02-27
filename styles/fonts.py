import pudu_ui


FONT_COLOR =  pudu_ui.colors.WHITE


def h1():
    style = pudu_ui.styles.fonts.h1()
    style.color = FONT_COLOR
    return style


def h2():
    style = pudu_ui.styles.fonts.h2()
    style.color = FONT_COLOR
    return style
