# AI:

* Prompt: Please write a Python static method called roll_dice within a class called game_logic that will accept only integers between 1 and 6 inclusive. It will output a tuple of length equal to the input value with random integers between 1 and 6 inclusive.

```python
import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        # raises warning if input is not an integer
        if not isinstance(num_dice, int):
            raise ValueError("Input must be an integer.")
        # raises warning if input is not between 1 and 6 exclusive
        # TODO: should be inclusive instead
        if num_dice < 1 or num_dice > 6:
            raise ValueError("Input must be between 1 and 6 inclusive.")
        # iterates number of input and generates a random number between 1 and 6, inclusive. formates as tuple
        dice_roll = tuple(random.randint(1, 6) for _ in range(num_dice))
        # returns/outputs results
        return dice_roll
```

* Prompt: User
Please write a static method for GameLogic called calculate_score that will accept an array of tuple integers between 1 and 6 inclusive and return one integer score. The score will be based on the following criteria: 6 unique integers is worth 1500, 3 unique pairs of integers is worth 1500, 3 equal integers is worth 100 multiplied by the integer unless that integer is 1 then it is worth 1000 multiplied by 1, if 4 equal integers perform the previous calculation and add that value to the sum for each additional integer that matches, if the score is zero after all this then count the number of integers equal to 5 add 50 to the score for each or if equal to 1 add 100 to the score. Return sum as integer

```python
class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        if not isinstance(dice_roll, list):
            raise ValueError("Input must be a list of tuple integers.")

        score = 0
        count = [0] * 7  # Initialize a list to count the occurrences of each integer (1 to 6)

        for die in dice_roll:
            if not isinstance(die, tuple):
                raise ValueError("Each element in the input list must be a tuple of integers.")
            
            if len(die) != 1:
                raise ValueError("Each tuple should contain a single integer.")

            num = die[0]
            if num < 1 or num > 6:
                raise ValueError("Integers in the tuple must be between 1 and 6 inclusive.")

            count[num] += 1

        # Calculate the score based on the criteria
        for num in range(1, 7):
            if count[num] == 6:  # 6 unique integers
                return 1500
            elif count[num] >= 3:  # At least 3 of a kind
                if num == 1:
                    score += 1000 * (num if count[num] >= 3 else 0)  # 1000 points for three 1's
                else:
                    score += 100 * (num if count[num] >= 3 else 0)  # 100 points for three of any other number

                # Subtract 3 from the count for the current number
                count[num] -= 3

        # Calculate score for additional numbers
        score += count[1] * 100  # 100 points for each remaining 1
        score += count[5] * 50   # 50 points for each remaining 5

        return score
```