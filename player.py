"""
created by Nagaj at 06/06/2021
"""
from config import TurtleConfig, TURTLE_WHITE_COLOR

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290
TURTLE_SHAPE = "turtle"
UP = 90
UP_KEY = "Up"


class Player(TurtleConfig):
    def __init__(self, shape=TURTLE_SHAPE, position=STARTING_POSITION, color=TURTLE_WHITE_COLOR, *args, **kwargs):
        super().__init__(shape=shape, position=position, color=color, *args, **kwargs)
        self.setheading(UP)

    def move_to_up(self):
        self.forward(MOVE_DISTANCE)

    @property
    def is_win(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_collision_with_car(self, cars):
        return any(car.distance(self) < 25 for car in cars)
