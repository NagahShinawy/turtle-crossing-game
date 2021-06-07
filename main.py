"""
created by Nagaj at 06/06/2021
"""
import time

from car_manager import Car, CarManger, LEFT_KEY
from config import screen_setup
from player import Player, UP_KEY
from level import Level


# ###########################################
screen = screen_setup()
screen.listen()

# ###########################################
player = Player()
carmanager = CarManger()
lvl = Level()
screen.onkey(key=UP_KEY, fun=player.move_to_up)
# screen.onkey(key=LEFT_KEY, fun=carmanager.move_cars)
# ############################################


def play():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        carmanager.create_car()
        carmanager.move_cars()
        if player.is_win:
            player.start_again()
            lvl.next_level()
            break


def main():
    play()
    screen.exitonclick()


if __name__ == "__main__":
    main()
