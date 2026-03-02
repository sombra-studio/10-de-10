from dataclasses import dataclass
from pudu_ui import Label, LabelParams, Params, Widget
from pyglet.graphics import Batch


from styles.fonts import p1
from utils import format_time


@dataclass
class ScoreRowParams(Params):
    position: int = 1
    player_name: str = "undefined"
    time: float = 1000


class ScoreRowWidget(Widget):
    def __init__(
        self,
        params: ScoreRowParams | None = None,
        batch: Batch | None = None
    ):
        super().__init__(params=params, batch=batch)
        label_style = p1()
        time_str = format_time(params.time)
        text = f"{params.position}.\t {params.player_name}\t {time_str}"
        label_params = LabelParams(
            width=params.width, text=text, style=label_style
        )
        self.label = Label(label_params, batch=batch, parent=self)
        self.height = self.label.height
        self.children.append(self.label)

    def recompute(self):
        super().recompute()
        self.label.invalidate()
