import sys
from ten_thousand.game_logic import GameLogic

class Game:
    def __init__(self):
        self.current_score = 0
        self.current_round = 0
        self.bankable_points = 0
        self.remaining_dice = 6

    def quit_game(self):
        if self.current_round == 0:
            print('OK. Maybe another time')
        else:
            print(f'Thanks for playing. You earned {self.current_score} points')
        sys.exit()

    def calculate_banked_score(self, points):
        self.bankable_points += points

    def select_dice_to_keep(self, current_roll: tuple):
        print('Enter dice to keep, or (q)uit:')
        user_input = input('> ')
        selection = []

        if user_input == 'q':
            self.quit_game()

        for char in user_input:
            if int(char) in current_roll:
                selection.append(int(char))

        bankable = GameLogic.calculate_score(tuple(selection))
        print(f'You have {bankable} unbanked points and {len(current_roll) - len(selection)} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')

        response = input('> ')

        if response == 'b':
            self.calculate_banked_score(bankable)
            print(f'You banked {bankable} points in round {self.current_round}')
            self.current_score += bankable
            print(f'Total score is {self.current_score} points')
            self.start_new_round()
        elif response == 'r':
            self.continue_round()
        elif response == 'q':
            self.quit_game()

    def start_new_round(self):
        self.current_round += 1
        print(f'Starting round {self.current_round}')
        print(f'Rolling 6 dice... ')
        dice_roll = GameLogic.roll_dice(6)
        print('*** ' + ' '.join(map(str, dice_roll)) + ' ***')
        self.select_dice_to_keep(dice_roll)

    def continue_round(self):
        pass
        print(f'Rolling {self.remaining_dice} dice...')
        dice_roll = GameLogic.roll_dice(self.remaining_dice)
        print('***' + ' '.join(map(str, dice_roll)) + ' ***')
        self.select_dice_to_keep(dice_roll)

    def start_game(self):
        print('Welcome to Ten Thousand\n(y)es to play or (n)o to decline')
        response = input('> ')

        if response.lower() == 'y':
            self.start_new_round()
        elif response.lower() == 'n':
            self.quit_game()


if __name__ == "__main__":
    game = Game()
    game.start_game()


