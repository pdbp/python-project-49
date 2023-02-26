from random import randint
from .. import cli


def game():
    number = randint(1, 100)
    if (number % 2) == 0:
        r_answ = 'yes'
    else:
        r_answ = 'no'
    answ = cli.question(number)
    if answ == r_answ:
        print('Correct!')
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        return False
