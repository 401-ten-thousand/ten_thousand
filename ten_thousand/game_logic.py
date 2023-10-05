import random

class GameLogic():
    @staticmethod
    def roll_dice(num: int) -> tuple[int]:
        #TODO ask adam
        if not isinstance(num, int):
            raise TypeError('Roll dice must be an integer')
        if num < 1 or num > 6:
            raise ValueError('Roll dice must be between 1 and 6')
        dice_roll = []
        for _ in range(0,num):
            dice_roll.append(random.randint(1,6))
        return tuple(dice_roll)
