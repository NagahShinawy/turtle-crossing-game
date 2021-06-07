"""
created by Nagaj at 06/06/2021
"""
import time

from car_manager import CarManger
from config import screen_setup
from scoreboard import Scoreboard
from player import Player, UP_KEY

# ###########################################
screen = screen_setup()
screen.listen()

# ###########################################
player = Player()
carmanager = CarManger()
scoreboard = Scoreboard()
screen.onkey(key=UP_KEY, fun=player.move_to_up)


# ############################################


def play():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        carmanager.create_car()
        carmanager.move_cars()
        if player.is_collision_with_car(carmanager.cars):
            scoreboard.game_over()
            game_is_on = False
        if player.is_win:
            player.go_to_start()
            scoreboard.increase_score_and_level()
            carmanager.speedup()


def main():
    play()
    screen.exitonclick()


if __name__ == "__main__":
    main()
