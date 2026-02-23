from pudu_ui.layouts import ListLayout, ListLayoutParams
from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch
from pyglet.window import key


from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from widgets import TokenWidget


INTER_ITEM_SPACING = 32
LIST_HEIGHT = 80
NUM_TOKENS = 10
LIST_WIDTH = int(NUM_TOKENS * LIST_HEIGHT + 9 * INTER_ITEM_SPACING)
LIST_X = SCREEN_WIDTH / 2 - LIST_WIDTH / 2
LIST_Y = SCREEN_HEIGHT / 2 - LIST_HEIGHT / 2


class TokenList(ListLayout):
    def __init__(
        self,
        batch: Batch | None = None
    ):
        params = ListLayoutParams(
            x=LIST_X, y=LIST_Y, width=LIST_WIDTH, height=LIST_HEIGHT,
            inter_item_spacing=INTER_ITEM_SPACING
        )
        super().__init__(params, batch=batch)

    def on_key_press(self, symbol, _) -> EVENT_HANDLE_STATE:
        if super().on_key_press(symbol, _) == EVENT_UNHANDLED:
            if (
                symbol == key.ENTER or
                symbol == key.RETURN or
                symbol == key.SPACE
            ):
                item = self.get_current_item()
                if item and isinstance(item, TokenWidget):
                    if item.is_selected:
                        item.unselect()
                    else:
                        item.unfocus()
                        item.select()
                    return EVENT_HANDLED
        return EVENT_UNHANDLED
