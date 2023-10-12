import random

class GameLogic():
    def __init__(self, mock_rolls):
        self.mock_rolls = mock_rolls

    @staticmethod
    def roll_dice(num: int) -> tuple[int]:
        # raise error if wrong type is inputted
        if not isinstance(num, int):
            raise TypeError('Roll dice must be an integer')
        # raise error if input is outside of range
        if num < 0 or num > 6:
            raise ValueError('Roll dice must be between 1 and 6')

        dice_roll = []
        for _ in range(0,num):
            dice_roll.append(random.randint(1,6))
        return tuple(dice_roll)

    @staticmethod
    def calculate_score(dice_roll: tuple[int] = mock_rolls.pop(0)) -> int:
        # raise error if input is not tuple
        if not isinstance(dice_roll,tuple):
            raise TypeError('Can only calculate scores for dice rolls supplied in tuples.')

        # raise error if input tuple has any components other than integer
        if not all([isinstance(i, int) for i in dice_roll]):
            raise TypeError('Can only calculate scores for dice rolls with integer values.')

        # raise error if tuple is wrong size
        if len(dice_roll) < 0 or len(dice_roll) > 6:
            raise ValueError('Can only calculate scores for 1-6 dice rolls.')

        # raise error if tuple contains integers outside of range
        if any([True if i<1 or i>6 else False for i in dice_roll]):
            raise ValueError("Values inside of tuple fall outside")

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
        # find 3 unique values checking for 3 pairs
        elif len(counter.keys()) == 3 and all([True if value == 2 else False for value in counter.values()]):
            c_score = 1500
        # find trio+
        else:
            for key, value in counter.items():
                if value >= 3:
                    constant = (value - 3) + 1
                    if key == 1:
                        c_score += (key * 1000) * constant
                    else:
                        c_score += (key * 100) * constant

                # add 5 and/or 1 scores to total
                elif key == 5:
                    c_score += (value * 50)
                elif key == 1:
                    c_score += (value * 100)
        return c_score
