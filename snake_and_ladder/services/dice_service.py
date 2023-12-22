import random


class DiceService(object):
    def roll(self):
        return random.randint(1, 6)
