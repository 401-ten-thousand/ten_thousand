import random as rd
from collections import Counter

# class GameLogic():
#
#     @staticmethod
#     def roll_dice(int_n:int) -> tuple[int]:
#         """
#         Function accepts integer(int_n) of how many of 6-sided die.
#         Returns tuple with int_n integers.
#         :param int_num_roll is integer of dice to roll:
#         :return tuple of integers representing sides rolled:
#         """
#         list_return = []
#         for _ in range(0,int_n):
#             int_roll = rd.randint(1,6)
#             list_return.append(int_roll)
#         return tuple(list_return)
#
#
#     @staticmethod
#     def calculate_score(tuple_dice: tuple[int]) -> int:
#         """
#         Accepts tuple of integers representing the sides of dice rolls
#         Returns total score according to the rules of dice game Ten-Thousand.
#         :param tuple_dice is tuple of integers:
#         :return integer of total score:
#         """
#         # count number of rolls for each side
#         dict_count = Counter(tuple_dice)
#         # score to be returned
#         int_score = 0
#         # to find straight
#         int_singles = 0
#         # to find 3 pairs
#         int_pairs = 0
#
#         for int_side, int_count in dict_count.items():
#             # looking for straight or 3 pairs
#             if int_count == 1: int_singles += 1
#             if int_count == 2: int_pairs += 1
#
#             # summing trios
#             if int_count >= 3:
#                 int_const = (int_count - 3) + 1
#                 if int_side == 1:
#                     int_score += (1000 * int_side) * int_const
#                 else:
#                     int_score += (100 * int_side) * int_const
#
#             # summing 5s less than 3 rolls
#             elif int_side == 5:
#                 int_score += (50 * int_count)
#
#             # summing 1s less than 3 rolls
#             elif int_side == 1:
#                 int_score += (100 * int_count)
#
#         # looking for straight or 3 pair
#         if (int_singles == 6 or int_pairs == 3) and len(tuple_dice) == 6 and int_score < 1500:
#             int_score = 1500
#
#         # return accumulative score achieved
#         return int_score

import random

class GameLogic:
    @staticmethod
    def roll_dice(dice_count):
        if not 1 <= dice_count <= 6:
            raise ValueError("Number of dice should be between 1 and 6.")
        return tuple(random.randint(1, 6) for _ in range(dice_count))

    @staticmethod
    def calculate_score(dice):
        # if len(set(dice)) == 6 and sum(dice) == 21:
        #     return 1500
        #
        # counts = [0] * 7
        # for die in dice:
        #     counts[die] += 1
        #
        # if all(count == 2 for count in counts[1:7]):
        #     return 1500
        #
        # for i in range(1, 7):
        #     if counts[i] == 6:
        #         return 2400
        #
        # score = 0
        # for i in range(1, 7):
        #     if counts[i] >= 3:
        #         if i == 1:
        #             score += 1000 * (counts[i] - 2)
        #         else:
        #             score += i * 100 * (counts[i] - 2)
        #     if i == 5:
        #         score += counts[i] * 50
        #
        # for i in range(1, 7):
        #     if counts[i] == 4:
        #         return 1200
        #     if counts[i] == 2:
        #         for j in range(1, 7):
        #             if counts[j] == 2 and j != i:
        #                 return 1200
        #
        # return score

        if not dice:
            return 0

        counter_dice = Counter(dice)
        if len(counter_dice) == 6:
            return 1500
        if len(set(dice)) == 3 and all(value == 2 for value in counter_dice.values()):
            return 1500
        if len(set(dice)) == 2 and all(value == 3 for value in counter_dice.values()):
            return 1200

        score = 0
        for value, count in counter_dice.items():
            if value == 1:
                if count >= 3:
                    score += 1000 * (count - 2)
                if count <= 2:
                    score += 100 * count
            elif value == 5:
                if count >= 3:
                    score += 500 * (count - 2)
                if count <= 2:
                    score += 50 * count
            elif value in [2, 3, 4, 6] and count >= 3:
                score += value * 100 * (count - 2)

        return score


# Testing the roll_dice method
print(GameLogic.roll_dice(5))  # Example with 5 dice

