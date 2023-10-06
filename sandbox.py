roll_die = (1, 2, 3, 4, 5, 6)
counter = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
def calculate_score(dice_roll):
    if len(dice_roll) < 1 or len(dice_roll) > 6:
        raise ValueError('can only calculate scores for 1-6 dice rolls')
    counter = {}
    c_score = 0
    # make counter dictionary
    for index, value in enumerate(dice_roll):
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
    # find 6 unique values which means there is a straight
    if len(counter.keys()) == 6 and all([True if value == 1 else False for value in counter.values()]):
        c_score = 1500
        return c_score
    # find 3 unique values checking for 3 pairs
    if len(counter.keys()) == 3 and all([True if value == 2 else False for value in counter.values()]):
        c_score = 1500
        return c_score
print(calculate_score(roll_die))