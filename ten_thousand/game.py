from ten_thousand.game_logic import GameLogic
from collections import Counter

class Game():
    def __init__(self,calculate_score=GameLogic.calculate_score, roll_dice=GameLogic.roll_dice):
        self.unbanked_score = 0
        self.banked_score = 0
        self.kept_dice = ()
        self.round_num = 1
        self.calculate_score = calculate_score
        self.roll_dice = roll_dice
        self.rolled_dice = ()

    def end_game(self, discharge: str):
        if discharge == "dishonorable":
            print("OK. Maybe another time")
        else:
            print(f"Thanks for playing. You earned {self.banked_score} points")
        exit()

    def input_begin_game(self, str_prompt):
        while True:
            # print prompt and collect input
            print(str_prompt)
            user_input = input("> ")

            # if y then start game
            if user_input.lower() == 'y':
                break
            # default exit game if wrong input
            else:
                self.end_game('dishonorable')

    def is_valid_input(self, user_input):
        # input is all digits
        user_input = user_input.replace(" ","")
        if user_input.isdigit():
            # convert user input into tuple
            tuple_user_input = tuple(int(char) for char in user_input if char.isdigit())

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
            # print('testing...not valid input')
            return False

    def does_roll_add_points(self,tuple_rolled_dice:tuple=()) -> bool:
        # if no scorable points; continue to next round
        if self.calculate_score(tuple_rolled_dice) == 0:
            return False
        else:
            return True


    def input_keep_quit(self, str_prompt):
        # print prompt and collect input
        print(str_prompt)

        user_input = input("> ")

        # should the game end
        if user_input.lower() == 'q':
            self.end_game('honorable')

        # if user input is valid
        elif self.is_valid_input(user_input):
            # convert user input into tuple
            tuple_user_input = tuple(int(char) for char in user_input if char.isdigit())

            # update unbanked score
            self.kept_dice = self.kept_dice + tuple_user_input
            self.unbanked_score += self.calculate_score(tuple_user_input)

            # not cheater or typo
            return False

        else:
            # cheater or typo
            # print("cheater or typo")
            return True

    def input_roll_bank_quit(self, str_prompt):
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
            # if all dice kept, allow for 6 new dice
            if (len(self.kept_dice) % 6) == 0:
                self.kept_dice = ()
                self.rolled_dice = self.roll_dice(6)
            # otherwise roll remaining dice
            else:
                self.rolled_dice = self.roll_dice(6-(len(self.kept_dice) % 6))
            return True
        else:
            return False

    def round(self):
        # loop per round
        continue_round = True
        typo_cheater = False
        while continue_round:
            # if cheater was true skip this print
            if not typo_cheater:
                print(f"Rolling {len(self.rolled_dice)} dice...")
            else:
                # if cheater was true change it back
                typo_cheater = False

            print(f'*** {" ".join([str(integer) for integer in self.rolled_dice])} ***')

            # does roll add points
            continue_round = self.does_roll_add_points(self.rolled_dice)
            # if no points available with roll
            if not continue_round:
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                print(f"You banked 0 points in round {self.round_num}")
                print(f"Total score is {self.banked_score} points")
                break

            # keep or quit
            typo_cheater = self.input_keep_quit("Enter dice to keep, or (q)uit:")
            if typo_cheater:
                print("Cheater!!! Or possibly made a typo...")
                continue

            # round continues
            print(f"You have {self.unbanked_score} unbanked points and {6 if len(self.kept_dice) == 6 else 6-len(self.kept_dice)} dice remaining")
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

            self.rolled_dice = self.roll_dice(6)

            # each round
            self.round()

            # roll new dice
            self.unbanked_score = 0
            self.kept_dice = ()

            # end of round increment
            self.round_num += 1

        self.end_game('honorable')



if __name__ == "__main__":
    # inst_game_logic = GameLogic([(1,2,3,4,5,6),(1,1,2,2,3,3)])
    # new_game = Game(inst_game_logic.calculate_score, inst_game_logic.mock_roll_dice)
    new_game = Game()
    new_game.play()




