from dataclasses import dataclass
from enum import StrEnum


class Languages(StrEnum):
    ES = "Spanish"
    EN = "English"
    FR = "French"


@dataclass
class Settings:
    audio_volume: int = 80
    muted: bool = False
    language: Languages = Languages.EN
