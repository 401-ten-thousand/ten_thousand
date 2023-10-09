import sys
from ten_thousand.game_logic import GameLogic


def quit_game(current_score):
    print(f'Thanks for playing. You earned {current_score} points')
    end_game()


def calculate_banked_score(current_score, points):
    return current_score + points


def continue_round_new_roll(remaining_dice, current_score, current_round, bankable):
    print(f'Rolling {remaining_dice} dice...')
    dice_roll = GameLogic.roll_dice(remaining_dice)
    print('***' + ' '.join(map(str, dice_roll)) + ' ***')
    select_dice_to_keep(dice_roll, current_score, current_round, bankable)

def select_dice_to_keep(current_roll: tuple, current_score, current_round, bankable) -> list:
    """
    Select dice player wants to keep for the next round.
    """
    print('Enter dice to keep, or (q)uit:')
    user_input = input('> ')
    selection = []

    if user_input == 'q':
        quit_game(current_score)

    for char in user_input:
        if int(char) in current_roll:
            selection.append(int(char))

    bankable += GameLogic.calculate_score(tuple(selection))
    print(f'You have {bankable} unbanked points and {len(current_roll) - len(selection)} dice remaining')
    print('(r)oll again, (b)ank your points or (q)uit:')

    response = input('> ')

    if response == 'b':
        new_score = calculate_banked_score(current_score, bankable)
        print(f'You banked {bankable} points in round {current_round}')
        print(f'Total score is {new_score} points')
        start_new_round(new_score, current_round)
    elif response == 'r':
        # start_new_round(current_score, current_round)
        remaining_dice = len(current_roll) - len(selection)
        continue_round_new_roll(remaining_dice, current_score, current_round, bankable)
    elif response == 'q':
        quit_game(current_score)


def start_new_round(current_score, current_round=0, bankable=0):
    current_round += 1
    print(f'Starting round {current_round}')
    print(f'Rolling 6 dice...')
    dice_roll = GameLogic.roll_dice(6)
    print('*** ' + ' '.join(map(str, dice_roll)) + ' ***')
    select_dice_to_keep(dice_roll, current_score, current_round, bankable)


def start_game():
    current_score = 0
    print('Welcome to Ten Thousand\n(y)es to play or (n)o to decline')
    response = input('> ')

    if response.lower() == 'y':
        start_new_round(current_score)
    elif response.lower() == 'n':
        print('OK. Maybe another time')
        end_game()


def main():
    start_game()


def end_game():
    sys.exit()


if __name__ == "__main__":
    main()
