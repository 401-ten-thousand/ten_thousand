# TITLE:
401: Ten-Thousand

## AUTHORS:
Kiengchay Gomez
Jacob Bassett

## DESCRIPTION:
We are building the game Ten Thousand. You can learn more about the game here. [wiki](https://en.wikipedia.org/wiki/Dice_10000) Or play it here. [play](https://www.playonlinedicegames.com/farkle)

## RUN:
To run the script open a terminal navigate into the ten-thousand directory and run the follow command.

```zsh
python -m ten_thousand.game
```

## TEST:
To run all unit tests open a terminal navigate into the ten-thousand directory and run the follow command.

```zsh
# for all tests
pytest
# for sim tests only
pytest -k test_sim
# for tests regarding calculate score function
pytest -k test_calculate_score
# for tests regarding
pytest -k test_roll_dice
```

## BOTS:
We built some bots to play the game. You can review this code in the 'bots.py' file. If you would like to run these bots, open a terminal run the following command and expect something similar to the following.

```zsh
(.venv) ➜  ten-thousand git:(finish-bots) python bots.py
NervousNellie: 1000 games played with average score of 8255
Bank2650_Roll3_Bot: 1000 games played with average score of 10370
Bank2000_Roll3_Bot: 1000 games played with average score of 10234
Bank2000_Roll2_Bot: 1000 games played with average score of 10241
Bank500_Bot: 1000 games played with average score of 8584
```

## VERSION:
3.0.0

## DATES:
10/4/2023 to 10/16/2023

## TOOLS:
python==3.11
colorama==0.4.6
docopt==0.6.2
iniconfig==2.0.0
packaging==23.2
pluggy==1.3.0
pytest==7.4.2
pytest-watch==4.2.0
watchdog==3.0.0

