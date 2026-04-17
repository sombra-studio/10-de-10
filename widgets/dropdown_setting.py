from pudu_ui import Dropdown, DropdownParams, Label, LabelParams, Widget
from pudu_ui.dropdown_trigger import DropdownTriggerParams
from pudu_ui.label import LabelResizeType
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.graphics import Batch


from styles.fonts import b1


LABEL_WIDTH = 200


class DropdownSetting(Widget):
    def __init__(
        self,
        label_str: str,
        curr_language: str,
        languages: list[str],
        batch: Batch
    ):
        super().__init__(batch=batch)
        label_params = LabelParams(
            width=LABEL_WIDTH,
            text=label_str, resize_type=LabelResizeType.FIT, style=b1()
        )
        self.language = curr_language
        self.label = Label(params=label_params, batch=batch, parent=self)

        trigger_params = DropdownTriggerParams(text=curr_language)
        dropdown_params = DropdownParams(
            trigger_params=trigger_params,
            options=languages,
            on_select=self.on_select
        )
        dropdown_params.x = self.width - dropdown_params.width
        self.dropdown = Dropdown(
            params=dropdown_params, batch=batch, parent=self
        )
        self.dropdown.y -= self.dropdown.height
        self.dropdown.y += (
            self.dropdown.trigger.height -
            self.dropdown.trigger_container_margin
        )
        self.dropdown.invalidate()

        self.children.append(self.label)
        self.children.append(self.dropdown)

    def on_select(self, selected_language: str):
        self.language = selected_language

    def recompute(self):
        super().recompute()
        self.dropdown.x = self.width - self.dropdown.width
        self.label.height = self.height

    # Defer events to toggle widget

    def on_focus(self):
        super().on_focus()
        self.dropdown.focus()

    def on_unfocus(self):
        super().on_unfocus()
        self.dropdown.unfocus()

    def on_mouse_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.dropdown.on_mouse_press(*args)

    def on_mouse_motion(self, *args):
        return self.dropdown.on_mouse_motion(*args)

    def on_key_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.dropdown.on_key_press(*args)
