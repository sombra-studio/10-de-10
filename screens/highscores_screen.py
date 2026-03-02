from pudu_ui import Screen


from game import Score
from widgets import BackButton, Title


TITLE = "Mejores Tiempos"


class HighscoresScreen(Screen):
    def __init__(self, highscores: list[Score]):
        super().__init__("Highscores")
        self.title = Title(text=TITLE, batch=self.batch)
        self.button = BackButton(batch=self.batch)

        self.widgets.append(self.button)

