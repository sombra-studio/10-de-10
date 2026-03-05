import os
import pyglet
import unittest


from constants import APP_NAME
from game import Score
from utils import (
    HIGHSCORES_FILENAME, USER_NAME_FILENAME, get_highscores, write_highscores,
    get_user_name,
    write_user_name
)


class DataFilesTestCase(unittest.TestCase):
    def test_highscores(self):
        folder = pyglet.resource.get_data_path(APP_NAME)
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = os.path.join(folder, HIGHSCORES_FILENAME)
        temp = None
        if os.path.exists(filename):
            # If we already have highscores, temporarily save it in memory
            try:
                with open(filename, 'rt') as f:
                    temp = f.read()
            except IOError:
                raise Exception(
                    f"file {filename} couldn't been open for testing highscores"
                )

        highscores = [
            Score("sombra", 354.85),
            Score("HenrY", 491.02),
            Score("Rafa", 526.73),
            Score("Jochy", 883.20),
            Score("Caleb", 953.03),
        ]

        write_highscores(highscores)
        scores_from_file = get_highscores()

        for i, score in enumerate(scores_from_file):
            self.assertEqual(score.player_name, highscores[i].player_name)
            self.assertEqual(score.time, highscores[i].time)

        if temp:
            # Write the highscores back
            try:
                with open(filename, 'wt') as f:
                    f.write(temp)
            except IOError:
                raise Exception(
                    f"Couldn't write back {filename} after testing"
                )

    def test_user_name(self):
        folder = pyglet.resource.get_data_path(APP_NAME)
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = os.path.join(folder, USER_NAME_FILENAME)
        temp = None
        if os.path.exists(filename):
            # If there's a user name already, temporarily save it
            try:
                with open(filename, 'rt') as f:
                    temp = f.read()
            except IOError:
                raise Exception(
                    f"file {filename} couldn't been open for testing user name"
                )

        user_name = "Test user name"
        write_user_name(user_name)
        user_name_from_file = get_user_name()
        self.assertEqual(user_name, user_name_from_file)

        if temp:
            # Write back the user name to the file
            try:
                with open(filename, 'wt') as f:
                    f.write(temp)
            except IOError:
                raise Exception(
                    f"Couldn't write back {filename} after testing"
                )


if __name__ == '__main__':
    unittest.main()
