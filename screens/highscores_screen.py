from pudu_ui import Screen

from widgets import Title


TITLE = "Mejores Tiempos"


class HighscoresScreen(Screen):
    def __init__(self):
        super().__init__("Highscores")
        self.title = Title(text=TITLE, batch=self.batch)
