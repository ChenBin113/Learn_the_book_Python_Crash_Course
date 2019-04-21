from random import randint


class Dice():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """默认六面"""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
