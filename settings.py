from dataclasses import dataclass
from enums import Languages


@dataclass
class Settings:
    audio_volume: int = 80
    muted: bool = False
    language: Languages = Languages.EN
