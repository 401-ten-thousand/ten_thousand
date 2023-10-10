import sys
from game_logic import GameLogic
from collections import Counter

class Game():
    def __init__(self):
        self.unbanked_score = 0
        self.banked_score = 0
        self.rolled_dice = GameLogic.roll_dice(6)
        self.kept_dice = ()
        self.round_num = 1

    def end_game(self,discharge: str):
        if discharge == "dishonorable":
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing. You earned {self.banked_score} points")
        sys.exit()

    def input_begin_game(self,str_prompt):
        while True:
            # print prompt and collect input
            print(str_prompt)
            user_input = str(input("> "))

            # if y then start game
            if user_input.lower() == 'y':
                return
            # default exit game if wrong input
            else:
                self.end_game('dishonorable')

    def is_valid_input(self, user_input, tuple_user_input):
        # input is all digits
        if user_input.isdigit():
            # if exception raised; continue to next round
            try:
                int_user_input_score = GameLogic.calculate_score(tuple_user_input)
            except Exception:
                return False

            # if no scorable points or empty input; continue to next round
            if int_user_input_score == 0:
                return False

            # make counter dictionary of input with integers as keys
            counter_user_input = Counter(tuple_user_input)
            # convert rolled dice into counter
            counter_rolled_dice = Counter(self.rolled_dice)

            # check if all input character are in rolled dice and less than rolled dice counts
            for key, value in counter_user_input.items():
                if key in counter_rolled_dice:
                    # if input exceed proportion in rolled dice
                    if value > counter_rolled_dice[key]:
                        return False
                # if input not in rolled dice
                else:
                    return False

            # if passing all the above return tuple of new kept dice and their score
            return True

        # if not all digits
        else:
            return False

    def input_keep_quit(self, str_prompt):
        # print prompt and collect input
        print(str_prompt)

        user_input = input("> ")

        tuple_user_input = tuple(int(char) for char in user_input)

        # should the game end
        if user_input.lower() == 'q':
            self.end_game('honorable')

        # if user input is valid
        elif self.is_valid_input(user_input, tuple_user_input):
            # update kept dice
            self.kept_dice = self.kept_dice + tuple_user_input
            # update unbanked score
            self.unbanked_score = GameLogic.calculate_score(self.kept_dice)


            # if no dice left to roll
            if (6 - len(self.kept_dice)) == 0:
                self.banked_score += self.unbanked_score
                return False
            #otherwise roll remaining dice
            else:
                self.rolled_dice = GameLogic.roll_dice(6 - len(self.kept_dice))
                return True
        else:
            return False

    def input_roll_bank_quit(self,str_prompt):
        # print prompt and collect input
        print(str_prompt)
        user_input = input("> ")

        # should the game end
        if user_input.lower() == 'q':
            self.end_game('honorable')

        # bank score
        elif user_input.lower() == 'b':
            print(f"You banked {self.unbanked_score} points in round {self.round_num}")
            self.banked_score += self.unbanked_score
            print(f"Total score is {self.banked_score} points")
            return False

        # roll dice
        elif user_input.lower() == 'r':
            self.rolled_dice = GameLogic.roll_dice(6-len(self.kept_dice))
            return True
        else:
            return False

    def round(self):
        # loop per round
        continue_round = True
        while continue_round:
            print(f"Rolling {len(self.rolled_dice)} dice...")
            print(f'*** {" ".join([str(integer) for integer in self.rolled_dice])} ***')
            # keep or quit
            continue_round = self.input_keep_quit("Enter dice to keep, or (q)uit:")
            # if user input isn't is not valid or is non-scoring
            if continue_round is False: break
            # round continues
            print(f"You have {self.unbanked_score} unbanked points and {len(self.rolled_dice)} dice remaining")
            # roll, bank or quit
            continue_round = self.input_roll_bank_quit("(r)oll again, (b)ank your points or (q)uit:")

    def play(self):
        # print welcome statement
        print("Welcome to Ten Thousand")

        # should we begin game
        self.input_begin_game("(y)es to play or (n)o to decline")

        # the game
        while self.round_num < 21:
            # begin round
            print(f"Starting round {self.round_num}")

            # each round
            self.round()

            # roll new dice
            self.unbanked_score = 0
            self.kept_dice = ()
            self.rolled_dice = GameLogic.roll_dice(6)

            # end of round increment
            self.round_num += 1

        self.end_game('honorable')


new_game = Game()
new_game.play()



