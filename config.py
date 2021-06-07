"""
created by Nagaj at 06/06/2021
"""
from turtle import Screen, Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLACK = "black"
SCREEN_TITLE = "Turtle Crossing Game"

CENTER = (0, 0)
TURTLE_WHITE_COLOR = "WHITE"


def screen_setup():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(BLACK)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)  # stop/ turn of animation
    return screen


class TurtleConfig(Turtle):
    def __init__(self, shape, position, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create(shape, position, color)

    def create(self, shape, position, color):
        self.shape(shape)
        self.penup()
        self.color(color)
        self.goto(position)
