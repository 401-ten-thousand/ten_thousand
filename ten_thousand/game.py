import sys
from ten_thousand.game_logic import GameLogic


def quit(current_score):
    print(f'Thanks for playing. You earned {current_score} points')
    end_game()


def bank_score(current_score, points):
    return current_score + points


def select_dice(current_roll: tuple, current_score, current_round) -> [int,]:
    """
    method to select dice player wants to keep
    :param current_roll: string representing dice values player wants to keep for next round
    :return:  list of integers player keeps
    """
    # print(current_roll)
    print('Enter dice to keep, or (q)uit')
    keep_or_quit = input('> ')
    selection = []
    if keep_or_quit != 'q':
        for char in keep_or_quit:
            if int(char) in current_roll:
                selection.append(int(char))
        bankable = GameLogic.calculate_score(tuple(selection))
        print(f'You have {bankable} unbanked points and {len(current_roll)-len(selection)} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')
        response = input('> ')
        if response == 'b':
            new_score = bank_score(current_score, bankable)
            print(f'You banked {bankable} points in round {current_round}')
            print(f'Total score is {new_score}')
            new_round(new_score, current_round)
        if response == 'r':
            new_round(current_score, current_round)
        if response == 'q':
            quit(current_score)
    if keep_or_quit == 'q':
        quit(current_score)


def new_round(current_score, current_round=0):
    current_round += 1
    print(f'Starting round {current_round}')
    print(f'Rolling 6 dice ')
    dice_roll = GameLogic.roll_dice(6)
    # https://chat.openai.com/c/dbdf1145-f718-4039-a3ec-d3b035dde627
    print('*** ' + ' '.join(map(str, dice_roll)) + ' ***')
    select_dice(dice_roll, current_score, current_round)


def start_game():
    current_score = 0
    print('Welcome to Ten Thousand\n(y)es to play or (n)o to decline')
    response = input('> ')
    if response.lower() == 'y':
        new_round(current_score)
    if response == 'n':
        print('OK. Maybe another time')
        end_game()


def play():
    #start game
    start_game()



def end_game():
    sys.exit()



if __name__ == "__main__":
    play()