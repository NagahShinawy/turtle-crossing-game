"""
created by Nagaj at 06/06/2021
"""
import random

from config import TurtleConfig, TURTLE_WHITE_COLOR

COLORS = [
    "red",
    "green",
    "blue",
    "medium slate blue",
    "purple",
    "chartreuse",
    "brown",
    "deep pink",
    "yellow",
    "white",
    "deep pink",
    "medium violet red",
    "green yellow",
    "light sky blue",
    "dark turquoise",
    "pale violet red",
    "rosy brown",
    "cyan",
    "dark orange",
    "hot pink",
    "magenta",
    "orange"
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_STARTING_POSITION = (280, 0)
WEST = 180
LEFT_KEY = "Left"
CAR_SHAPE = "square"
CAR_SIZE = (20, 40)
STARTING_CAR_X_POINT = (250, 280)
STARTING_CAR_Y_POINT = (-250, 250)


class Car(TurtleConfig):
    def __init__(self, shape, position, color, *args, **kwargs):
        super().__init__(shape=shape, position=position, color=color, *args, **kwargs)
        self.shapesize(stretch_len=1.5, stretch_wid=.5)


class CarManger:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_x = random.randint(*STARTING_CAR_X_POINT)
        random_y = random.randint(*STARTING_CAR_Y_POINT)
        new_car = Car(shape=CAR_SHAPE, position=(random_x, random_y), color=random.choice(COLORS))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
