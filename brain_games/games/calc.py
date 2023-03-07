from random import randint
from random import choice


def game():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    seqence = ('+', '-', '*')
    sign = choice(seqence)
    expression = f'{str(number1)} {choice(sign)} {str(number2)}'
    if sign == '+':
        r_answ = str(number1 + number2)
    elif sign == '-':
        r_answ = str(number1 - number2)
    else:
        r_answ = str(number1 * number2)
    return expression, r_answ


def rules():
    return 'What is the result of the expression?'
