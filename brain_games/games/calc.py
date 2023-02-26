from random import randint
from random import choice
from .. import cli


def game():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    seqence = ('+', '-', '*')
    sign = choice(seqence)
    expression = str(number1) + ' ' + choice(sign) + ' ' + str(number2)
    if sign == '+':
        r_answ = str(number1 + number2)
    elif sign == '-':
        r_answ = str(number1 - number2)
    else:
        r_answ = str(number1 * number2)
    answ = cli.question(expression)
    if answ == r_answ:
        print('Correct!')
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        return False
