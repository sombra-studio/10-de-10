from pudu_ui import Label, LabelParams, Params, Slider, SliderParams, Widget
from pudu_ui.label import LabelResizeType
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.graphics import Batch


from styles.fonts import b1, p1

LABEL_WIDTH = 200
SLIDER_X = LABEL_WIDTH + 50
SLIDER_WIDTH = 250
VALUE_X = SLIDER_X + SLIDER_WIDTH + 20
HEIGHT = 48


class SliderSetting(Widget):
    def __init__(self, label_str: str, value: float, batch: Batch):
        params = Params(height=HEIGHT)
        super().__init__(params=params)
        label_params = LabelParams(
            width=LABEL_WIDTH, height=self.height, text=label_str,
            resize_type=LabelResizeType.FIT, style=b1()
        )
        self.label = Label(label_params, batch=batch, parent=self)

        slider_params = SliderParams(
            x=SLIDER_X, width=SLIDER_WIDTH,
            value=value, on_value_changed=self.on_value_changed
        )
        self.slider = Slider(slider_params, batch=batch, parent=self)

        value_label_params = LabelParams(
            x=VALUE_X, height=self.height, text=f"{value}",
            resize_type=LabelResizeType.FIT, style=p1()
        )
        self.value_label = Label(value_label_params, batch=batch, parent=self)

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
