"""
created by Nagaj at 06/06/2021
"""
from turtle import Turtle

FONT = ("Courier", 13, "normal")
CENTER = "center"
SCORE_POSITION = (-250, 250)
SCORE_INFO = "Score : {score}\nLevel : {level}"
GAME_OVER = "GAME OVER"
DEFAULT_POSITION = 0, 0
WHITE = "white"


class Dashboard(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = 0
        self.level = 1
        self.score_info = SCORE_INFO
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color(WHITE)
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_scoreboard(
            text=self.score_info.format(score=self.score, level=self.level)
        )

    def increase_score_and_level(self):
        self.score += 1
        self.level += 1
        self.clear()
        self.update_scoreboard(
            text=self.score_info.format(score=self.score, level=self.level)
        )

    def update_scoreboard(self, text):
        self.write(text, align=CENTER, font=FONT)

    def game_over(self):
        self.goto(DEFAULT_POSITION)
        self.update_scoreboard(text=GAME_OVER)
