"""
created by Nagaj at 06/06/2021
"""
import random

from config import TurtleConfig

CAR_STARTING_POSITION = (280, 0)
WEST = 180
LEFT_KEY = "Left"


class Car(TurtleConfig):
    def __init__(self, shape="turtle", position=CAR_STARTING_POSITION, *args, **kwargs):
        super().__init__(shape=shape, position=position, *args, **kwargs)
        self.setheading(WEST)

    def move_to_left(self):
        self.forward(random.randint(10, 20))
