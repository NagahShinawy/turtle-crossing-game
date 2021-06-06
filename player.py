"""
created by Nagaj at 06/06/2021
"""
from config import TurtleConfig

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_SHAPE = "turtle"
UP = 90
UP_KEY = "Up"


class Player(TurtleConfig):
    def __init__(self, shape=TURTLE_SHAPE, position=STARTING_POSITION, *args, **kwargs):
        super().__init__(shape=shape, position=position, *args, **kwargs)
        self.setheading(UP)

    def move_to_up(self):
        self.forward(MOVE_DISTANCE)
