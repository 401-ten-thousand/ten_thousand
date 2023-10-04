import random as rd
from collections import Counter

class GameLogic():

    @staticmethod
    def roll_dice(int_n:int) -> tuple[int]:
        """
        Function accepts integer(int_n) of how many of 6-sided die.
        Returns tuple with int_n integers.
        :param int_num_roll is integer of dice to roll:
        :return tuple of integers representing sides rolled:
        """
        list_return = []
        for _ in range(0,int_n):
            int_roll = rd.randint(1,6)
            list_return.append(int_roll)
        return tuple(list_return)


    @staticmethod
    def calculate_score(tuple_dice: tuple[int]) -> int:
        """
        Accepts tuple of integers representing the sides of dice rolls
        Returns total score according to the rules of dice game Ten-Thousand.
        :param tuple_dice is tuple of integers:
        :return integer of total score:
        """
        # count number of rolls for each side
        dict_count = Counter(tuple_dice)
        # score to be returned
        int_score = 0
        # to find straight
        int_singles = 0
        # to find 3 pairs
        int_pairs = 0

        for int_side, int_count in dict_count.items():
            # looking for straight or 3 pairs
            if int_count == 1: int_singles += 1
            if int_count == 2: int_pairs += 1

            # summing trios
            if int_count >= 3:
                int_const = (int_count - 3) + 1
                if int_side == 1:
                    int_score += (1000 * int_side) * int_const
                else:
                    int_score += (100 * int_side) * int_const

            # summing 5s less than 3 rolls
            elif int_side == 5:
                int_score += (50 * int_count)

            # summing 1s less than 3 rolls
            elif int_side == 1:
                int_score += (100 * int_count)

        # looking for straight or 3 pair
        if (int_singles == 6 or int_pairs == 3) and len(tuple_dice) == 6 and int_score < 1500:
            int_score = 1500

        # return accumulative score achieved
        return int_score