import getpass
from io import TextIOWrapper
import pyglet
import os


from constants import APP_NAME
from game import Score
from settings import Languages, Settings


HIGHSCORES_FILENAME = "highscores.txt"
SETTINGS_FILENAME = "settings.txt"
USER_NAME_FILENAME = "user_name.txt"


def format_time(time: float) -> str:
    minutes, seconds = divmod(time, 60)
    return "%02d:%02d" % (minutes, seconds)


def write_data_file(filename: str) -> TextIOWrapper:
    folder = pyglet.resource.get_data_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, filename)
    file = open(filename, 'wt')
    return file


def write_highscores(highscores: list[Score]):
    with write_data_file(HIGHSCORES_FILENAME) as f:
        lines = []
        for score in highscores:
            lines.append(score.player_name + "\n")
            lines.append(f"{score.time:.2f}\n")
        f.writelines(lines)


def write_settings(settings: Settings):
    folder = pyglet.resource.get_settings_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, SETTINGS_FILENAME)
    with open(filename, 'wt') as f:
        f.write(
            f"{settings.audio_volume}\n"
            f"{"m" if settings.muted else " "}\n"
            f"{settings.language}"
        )


def write_user_name(user_name: str):
    with write_data_file(USER_NAME_FILENAME) as f:
        f.write(user_name)


def get_highscores() -> list[Score]:
    """
    Get the highscores from a given .txt file that will be like this:
        "
            Henry
            323.11
            Rafa
            486.21
            ...
        "

    Returns:
        list[Score]: An ordered list of the best scores
    """
    high_scores: list[Score] = []
    folder = pyglet.resource.get_data_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, HIGHSCORES_FILENAME)
    try:
        with open(filename, 'rt') as f:
            curr_line_is_name = True
            for line in f:
                if curr_line_is_name:
                    new_score = Score(player_name=line[:-1])
                    high_scores.append(new_score)
                else:
                    high_scores[-1].time = float(line)
                curr_line_is_name = not curr_line_is_name
    except IOError:
        pass
    return high_scores


def get_settings() -> Settings:
    folder = pyglet.resource.get_settings_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, SETTINGS_FILENAME)
    settings = Settings()
    try:
        with open(filename, 'rt') as f:
            lines = [line.strip() for line in f]
            settings = Settings(
                int(lines[0]),
                lines[1] == 'm',
                Languages(lines[2])
            )
            return settings
    except IOError:
        pass
    return settings


def get_user_name() -> str:
    folder = pyglet.resource.get_data_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, USER_NAME_FILENAME)
    try:
        with open(filename, 'rt') as f:
            user_name = f.read()
    except IOError:
        try:
            user_name = getpass.getuser()
        except OSError:
            user_name = "Undefined"
    return user_name
