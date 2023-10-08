import sys
from game_logic import GameLogic
from collections import Counter

class Game():
    def __init__(self):
        self.unbanked_score = 0
        self.banked_score = 0
        self.rolled_dice = GameLogic.roll_dice(6)
        self.rolled_dice_counter = Counter(self.rolled_dice)
        self.kept_dice = ()
        self.round_num = 0

    def end_game(self,discharge: str):
        if discharge == "dishonorable":
            print("OK. Maybe another time.")
        else:
            print(f"Thanks for playing. You earned {self.banked_score} points")
        sys.exit()

    def input_begin_game(self,str_prompt):
        count = 0

        while count < 20:
            # print prompt and collect input
            print(str_prompt)
            user_input = str(input("> "))

            # if y then start game
            if user_input.lower() == 'y':
                return 1
            # if n then exit game
            elif user_input.lower() == 'n':
                self.end_game('dishonorable')
            count += 1

        # incase count exceed limit, exit game
        self.end_game('honorable')

    def input_keep_quit(self, str_prompt):
        count = 0

        while count < 20:
            # print prompt and collect input
            print(str_prompt)
            user_input = str(input("> "))

            # should the game end
            if user_input.lower() == 'q':
                self.end_game('honorable')

            # are all input characters convertable to digits
            elif user_input.isdigit():
                # make counter dictionary of input with integers as keys
                dict_user_input = Counter([int(char) for char in user_input])

                # check if all input character are in rolled dice and less than rolled dice counts
                bool_update_kept_dice = True
                for key, value in dict_user_input.items():
                    if key in self.rolled_dice_counter:
                        if value > self.rolled_dice_counter[key]:
                            bool_update_kept_dice = False
                    else:
                        bool_update_kept_dice = False

                # only update if all input character are in rolled dice and less than rolled dice counts
                if bool_update_kept_dice:
                    # update kept dice
                    for key, value in dict_user_input.items():
                        tuple_to_extend = tuple([key]*value)
                        self.kept_dice = self.kept_dice + tuple_to_extend

                    # roll dice again
                    self.rolled_dice = GameLogic.roll_dice(6 - len(self.kept_dice))
                    self.rolled_dice_counter = Counter(self.rolled_dice)

                    # update unbanked score
                    self.unbanked_score = GameLogic.calculate_score(self.kept_dice)
                return

            # increment to limit just in case this takes all day
            count += 1

    def input_roll_bank_quit(self,str_prompt):
        count = 0

        while count < 20:
            # print prompt and collect input
            print(str_prompt)
            user_input = str(input("> "))

            # should the game end
            if user_input.lower() == 'q':
                self.end_game('honorable')
                return False

            # bank score
            elif user_input.lower() == 'b':
                print(f"You banked {self.unbanked_score} points in round {self.round_num}")
                self.banked_score += self.unbanked_score
                print(f"Total score is {self.banked_score} points")
                self.unbanked_score = 0
                self.kept_dice = ()
                self.rolled_dice = GameLogic.roll_dice(6)
                self.rolled_dice_counter = Counter(self.rolled_dice)
                return  False

            # roll dice
            elif user_input.lower() == 'r':
                self.rolled_dice = GameLogic.roll_dice(6-len(self.kept_dice))
                self.rolled_dice_counter = Counter(self.rolled_dice)
                return True

            # increment to limit just in case this takes all day
            count += 1

    def play(self):
        print("Welcome to Ten Thousand")

        self.round_num = self.input_begin_game("(y)es to play or (n)o to decline")

        while self.round_num > 0:
            print(f"Starting round {self.round_num}")

            # loop per round
            continue_round = True
            while continue_round:
                print(f"Rolling {len(self.rolled_dice)} dice...")
                print(f'*** {" ".join([str(integer) for integer in self.rolled_dice])} ***')
                self.input_keep_quit("Enter dice to keep, or (q)uit:")
                print(f"You have {self.unbanked_score} unbanked points and {len(self.rolled_dice)} dice remaining")
                continue_round = self.input_roll_bank_quit("(r)oll again, (b)ank your points or (q)uit:")


            # end of round increment
            self.round_num += 1



# new_game = Game()
# new_game.play()



