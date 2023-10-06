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

    @staticmethod
    def calculate_score(dice_roll: tuple[int]) -> int:
        if len(dice_roll) < 0 or len(dice_roll) > 6:
            raise ValueError('can only calculate scores for 1-6 dice rolls')
        counter = {}
        c_score = 0
        # make counter dictionary
        for index, value in enumerate(dice_roll):
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1
        # find 6 unique values which means there is a straight
        if len(counter.keys()) == 6 and all([True if value == 1 else False for value in counter.values()]):
            c_score = 1500
            return c_score
        # find 3 unique values checking for 3 pairs
        if len(counter.keys()) == 3 and all([True if value == 2 else False for value in counter.values()]):
            c_score = 1500
            return c_score
        # {2: 4, 1: 1, 5: 1}
        # find trio+
        for key, value in counter.items():
            if value >= 3:
                constant = (value - 3) + 1
                if key == 1:
                    c_score += (key * 1000) * constant
                else:
                    c_score += (key * 100) * constant
            elif key == 5:
                c_score += (value * 50)
            elif key == 1:
                c_score += (value * 100)
        return c_score
