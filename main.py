"""
created by Nagaj at 06/06/2021
"""
import time

from config import screen_setup
from player import Player, UP_KEY


screen = screen_setup()


def play():
    screen.listen()
    player = Player()
    screen.onkey(key=UP_KEY, fun=player.move_to_up)
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()


def main():
    play()
    screen.exitonclick()


if __name__ == "__main__":
    main()
