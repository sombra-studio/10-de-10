from collections.abc import Callable
from pudu_ui import Screen
from pudu_ui.layouts import ListDirection, ListLayout, ListLayoutParams

from constants import (
    AUDIO_VOLUME_S, CANCEL_S, CONTINUE_S, SCREEN_WIDTH,
    SETTINGS, SETTINGS_S
)
from settings import Settings
from styles.buttons import BUTTON_HEIGHT
from widgets import CancelButton, ContinueButton, SliderSetting, Title
from widgets.buttons.cancel_button import BUTTON_Y


LIST_WIDTH = 600
LIST_HEIGHT = 350
LIST_Y = BUTTON_Y + BUTTON_HEIGHT + 20


class SettingsScreen(Screen):
    def __init__(self, settings: Settings, get_text: Callable[str, str]):
        super().__init__(SETTINGS)

        self.title = Title(text=get_text(SETTINGS_S), batch=self.batch)

        layout_params = ListLayoutParams(
            x=SCREEN_WIDTH // 2 - LIST_WIDTH // 2,
            y=LIST_Y,
            width=LIST_WIDTH,
            height=LIST_HEIGHT,
            direction=ListDirection.VERTICAL,
            resizes_item_width=False,
            resizes_item_height=False
        )
        self.layout = ListLayout(params=layout_params, batch=self.batch)

        # Audio volume settings
        self.audio_volume_setting = SliderSetting(
            label_str=get_text(AUDIO_VOLUME_S),
            value=settings.audio_volume,
            batch=self.batch
        )

        self.layout.add(self.audio_volume_setting)
        self.widgets.append(self.layout)

        # Continue and cancel buttons
        self.button = ContinueButton(batch=self.batch)
        self.button.text = get_text(CONTINUE_S)
        self.button.invalidate()

        self.cancel_button = CancelButton(batch=self.batch)
        self.cancel_button.text = get_text(CANCEL_S)
        self.cancel_button.invalidate()

        self.widgets.append(self.button)
        self.widgets.append(self.cancel_button)
