"""
created by Nagaj at 07/06/2021
"""


class Level:
    def __init__(self):
        self.level = 1

    def next_level(self):
        print(f"You are now in the level {self.level + 1}")
        return self.level + 1

    @property
    def current_level(self):
        return self.level
