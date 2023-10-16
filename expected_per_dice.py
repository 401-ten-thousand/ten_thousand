from ten_thousand.game_logic import GameLogic
from statistics import mean

dict_expected_value_per_dice = {1:[],2:[],3:[],4:[],5:[],6:[]}

for i in range(1,7):
    for _ in range(0,100):
        roll = GameLogic.roll_dice(i)
        score = GameLogic.calculate_score(roll)
        dict_expected_value_per_dice[i].append(score)



for key,value in dict_expected_value_per_dice.items():
    print(key)
    print(mean(value))