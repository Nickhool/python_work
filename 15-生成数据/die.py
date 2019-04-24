__Author__ = "noduez"

from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_side=6):
        """骰子默认为6面"""
        self.num_sides = num_side

    def roll(self):
        """返回一个1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)