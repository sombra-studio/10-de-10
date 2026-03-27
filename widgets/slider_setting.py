from pudu_ui import Label, LabelParams, Slider, SliderParams, Widget
from pudu_ui.label import LabelResizeType
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.graphics import Batch


from styles.fonts import b1, p1


LABEL_WIDTH = 200
SLIDER_WIDTH = 250
SLIDER_VALUE_MARGIN = 20


class SliderSetting(Widget):
    def __init__(self, label_str: str, value: float, batch: Batch):
        super().__init__(batch=batch)
        label_params = LabelParams(
            width=LABEL_WIDTH, text=label_str,
            resize_type=LabelResizeType.FIT, style=b1()
        )
        self.label = Label(label_params, batch=batch, parent=self)

        slider_params = SliderParams(
            width=SLIDER_WIDTH,
            value=value, on_value_changed=self.on_value_changed
        )
        self.slider = Slider(slider_params, batch=batch, parent=self)

        value_label_params = LabelParams(
            x=self.width, anchor_x='right', text=f"{value}",
            resize_type=LabelResizeType.FIT, style=p1()
        )
        self.value_label = Label(value_label_params, batch=batch, parent=self)
        self.value_label.width = 60

        self.children.append(self.label)
        self.children.append(self.slider)
        self.children.append(self.value_label)

    @property
    def value(self) -> float:
        return self.slider.value

    def on_value_changed(self, slider: Slider):
        self.value_label.text = f"{int(slider.value)}"
        self.value_label.invalidate()

    def on_mouse_press(self, *args) -> EVENT_HANDLE_STATE:
        return self.slider.on_mouse_press(*args)

    def on_mouse_release(self, *args) -> EVENT_HANDLE_STATE:
        return self.slider.on_mouse_release(*args)

    def on_mouse_drag(self, *args) -> bool:
        return self.slider.on_mouse_drag(*args)

    def recompute(self):
        super().recompute()
        self.value_label.x = self.width
        self.slider.x = (
            self.width - self.value_label.impl.content_width -
            SLIDER_VALUE_MARGIN - self.slider.width
        )
        self.label.height = self.height
        self.value_label.height = self.height
