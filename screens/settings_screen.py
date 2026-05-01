from collections.abc import Callable
from pudu_ui import Screen
from pudu_ui.layouts import ListDirection, ListLayout, ListLayoutParams

from constants import (
    AUDIO_ON_S, AUDIO_VOLUME_S, CANCEL_S, CONTINUE_S, LANGUAGE_S, SCREEN_WIDTH,
    SETTINGS, SETTINGS_S
)
from enums import Languages
from settings import Settings
from styles.buttons import BUTTON_HEIGHT
from widgets import (
    CancelButton, ContinueButton, DropdownSetting, SliderSetting, Title,
    ToggleSetting
)
from widgets.buttons.cancel_button import BUTTON_Y


LIST_WIDTH = 800
LIST_HEIGHT = 350
LIST_Y = BUTTON_Y + BUTTON_HEIGHT + 20
INTER_ITEM_SPACING = 12
ITEM_HEIGHT = 48


class SettingsScreen(Screen):
    def __init__(self, settings: Settings, get_text: Callable[[str], str]):
        super().__init__(SETTINGS)

        self.title = Title(text=get_text(SETTINGS_S), batch=self.batch)

        layout_params = ListLayoutParams(
            x=SCREEN_WIDTH // 2 - LIST_WIDTH // 2,
            y=LIST_Y,
            width=LIST_WIDTH,
            height=LIST_HEIGHT,
            direction=ListDirection.VERTICAL,
            inter_item_spacing=INTER_ITEM_SPACING,
            item_height=ITEM_HEIGHT
        )
        self.layout = ListLayout(params=layout_params, batch=self.batch)

        # Audio volume settings
        self.audio_volume_setting = SliderSetting(
            label_str=get_text(AUDIO_VOLUME_S),
            value=settings.audio_volume,
            batch=self.batch
        )

        # Audio on setting
        self.audio_on_setting = ToggleSetting(
            label_str=get_text(AUDIO_ON_S),
            is_on=not settings.muted,
            batch=self.batch
        )

        # Language setting
        self.language_setting = DropdownSetting(
            label_str=get_text(LANGUAGE_S),
            curr_language=settings.language,
            languages=[language for language in Languages],
            batch=self.batch
        )

        self.layout.add(self.audio_volume_setting)
        self.layout.add(self.audio_on_setting)
        self.layout.add(self.language_setting)
        self.widgets.append(self.layout)

        # Continue and cancel buttons
        self.button = ContinueButton(self.batch, get_text)

        self.cancel_button = CancelButton(self.batch, get_text)

        self.widgets.append(self.button)
        self.widgets.append(self.cancel_button)

    def get_settings(self) -> Settings:
        settings = Settings(
            audio_volume=int(self.audio_volume_setting.value),
            muted=not self.audio_on_setting.toggle.is_on,
            language=Languages(self.language_setting.language)
        )
        return settings
