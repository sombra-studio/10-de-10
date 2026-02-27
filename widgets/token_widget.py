from collections.abc import Callable
from copy import copy
from pudu_ui import Color, Frame
from pudu_ui.colors import WHITE, DARK_RED
from pudu_ui.styles.frames import FrameStyle
import pudu_ui
from pyglet.graphics import Batch
from pyglet.window import mouse
import pyglet


from styles.tokens import TokenStyle


DEFAULT_TOKEN_COLOR = pudu_ui.colors.GRAY
TOKEN_BORDER_WIDTH = 5
TOKEN_BORDER_RADIUS = 12


class TokenWidget(Frame):
    def __init__(
        self, color: Color = DEFAULT_TOKEN_COLOR,
        on_select_callback: Callable[[int], None] = lambda l: None,
        batch: Batch | None = None
    ):
        super().__init__(batch=batch)
        self.is_focusable = True
        self.is_selected = False
        self.on_select_callback = on_select_callback

        unfocused_border_width = 0
        unfocused_border_color = WHITE
        self.unfocused_style = TokenStyle(
            color=color,
            border_width=unfocused_border_width,
            border_color=unfocused_border_color
        )

        focused_border_width = TOKEN_BORDER_WIDTH
        self.focused_style = copy(self.unfocused_style)
        self.focused_style.border_width = focused_border_width

        self.hovered_style = copy(self.unfocused_style)
        self.hovered_style.color *= 0.7

        self.selected_style = copy(self.focused_style)
        self.selected_style.border_color = DARK_RED

        self.change_style(self.unfocused_style)

    def change_style(self, style: TokenStyle):
        frame_style = FrameStyle()
        frame_style.set_solid_color(style.color)
        frame_style.set_uniform_radius(TOKEN_BORDER_RADIUS)
        frame_style.border_color = style.border_color
        frame_style.border_width = style.border_width
        super().change_style(frame_style)

    def on_focus(self):
        super().on_focus()
        self.change_style(self.focused_style)

    def on_unfocus(self):
        super().on_unfocus()
        self.change_style(self.unfocused_style)

    def on_hover(self):
        super().on_hover()
        self.change_style(self.hovered_style)

    def on_unhover(self):
        super().on_unhover()
        self.change_style(self.unfocused_style)

    def on_select(self):
        self.invalidate()
        self.change_style(self.selected_style)

    def on_unselect(self):
        self.invalidate()
        self.change_style(self.unfocused_style)

    def select(self):
        self.is_selected = True
        self.is_on_hover = False
        # HACK
        self.is_on_focus = True
        self.on_select()
        self.on_select_callback(self.index)

    def unselect(self):
        self.is_selected = False
        # HACK
        self.is_on_focus = False
        self.on_unselect()
    
    def unfocus(self):
        if not self.is_selected:
            super().unfocus()

    # Override function
    def on_mouse_press(self, x, y, buttons, _):
        if self.is_inside(x, y) and buttons & mouse.LEFT:
            if not self.is_selected:
                self.select()
            else:
                self.unselect()
                self.hover()
            return pyglet.event.EVENT_HANDLED
        return pyglet.event.EVENT_UNHANDLED
