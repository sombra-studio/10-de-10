from pudu_ui import Label, LabelParams, Toggle, ToggleParams, Widget
from pudu_ui.label import LabelResizeType
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.graphics import Batch


from styles.fonts import b1


LABEL_WIDTH = 200


class ToggleSetting(Widget):
    def __init__(self, label_str: str, is_on: bool, batch: Batch):
        super().__init__(batch=batch)
        label_params = LabelParams(
            width=LABEL_WIDTH,
            text=label_str, resize_type=LabelResizeType.FIT, style=b1()
        )
        self.label = Label(params=label_params, batch=batch, parent=self)

        toggle_params = ToggleParams(is_on=is_on)
        toggle_params.x = self.width - toggle_params.width
        self.toggle = Toggle(params=toggle_params, batch=batch, parent=self)

        self.children.append(self.label)
        self.children.append(self.toggle)

    def recompute(self):
        super().recompute()
        self.toggle.x = self.width - self.toggle.width
        self.label.height = self.height

    # Defer events to toggle widget

    def on_focus(self):
        super().on_focus()
        self.toggle.focus()

    def on_unfocus(self):
        super().on_unfocus()
        self.toggle.unfocus()

    def on_mouse_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.toggle.on_mouse_press(*args)

    def on_mouse_motion(self, *args):
        return self.toggle.on_mouse_motion(*args)

    def on_key_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.toggle.on_key_press(*args)
