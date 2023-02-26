from random import randint
from math import gcd
from .. import cli


def game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    r_answ = str(gcd(number1, number2))
    question = str(number1) + ' ' + str(number2)
    answ = cli.question(question)
    if answ == r_answ:
        print('Correct!')
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        return False
