import os
import pyglet
import unittest


from constants import APP_NAME
from settings import Languages, Settings
from utils import SETTINGS_FILENAME, get_settings, write_settings


class SettingsTestCase(unittest.TestCase):
    def test_settings(self):
        folder = pyglet.resource.get_settings_path(APP_NAME)
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = os.path.join(folder, SETTINGS_FILENAME)
        temp = None
        if os.path.exists(filename):
            # If we already have settings, temporarily save it in memory
            try:
                with open(filename, 'rt') as f:
                    temp = f.read()
            except IOError:
                raise Exception(
                    f"file {filename} couldn't been open for testing settings"
                )

        settings = Settings(audio_volume=50, muted=False, language=Languages.ES)
        write_settings(settings)

        settings_from_file = get_settings()
        self.assertEqual(settings, settings_from_file)

        if temp:
            # Write the settings back
            try:
                with open(filename, 'wt') as f:
                    f.write(temp)
            except IOError:
                raise Exception(
                    f"Couldn't write back {filename} after testing"
                )
        else:
            # Remove the file created for this test
            try:
                os.remove(filename)
                print(f"File '{filename}' has been deleted.")
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")
            except PermissionError:
                print(
                    f"Error: Permission denied to delete the file '{filename}'."
                )
            except OSError as e:
                print(f"Error occurred: {e.strerror}")


if __name__ == '__main__':
    unittest.main()
