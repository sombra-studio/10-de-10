from io import TextIOWrapper

import pyglet
import os


from constants import APP_NAME


def format_time(time: float) -> str:
    minutes, seconds = divmod(time, 60)
    return "%02d:%02d" % (minutes, seconds)


def open_highscores_file() -> TextIOWrapper:
    folder = pyglet.resource.get_data_path(APP_NAME)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, 'highscores.txt')
    file = open(filename, 'r+t')
    return file


def get_highscores(f: TextIOWrapper) -> dict[str, float]:
    """
    Get the highscores from a given .txt file
    Args:
        f: A .txt file that will come like this:
            "
                Henry
                323.11
                Rafa
                486.21
                ...
            "
    Returns:
        dict[str, float]: A dictionary with the name of the user as a key and
            its time in seconds as a float
    """
    high_scores = {}
    name = None
    for line in f:
        if name:
            high_scores[name] = float(line)
            name = None
        else:
            name = line
    return high_scores
