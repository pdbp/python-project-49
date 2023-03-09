from random import randint
from random import choice
RULES = 'What is the result of the expression?'


def game():
    START_RAND_NUMB_RANGE = 1
    END_RAND_NUMB_RANGE = 25
    number1 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    number2 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    RAND_SIGNS_RANGE = ('+', '-', '*')
    sign = choice(RAND_SIGNS_RANGE)
    expression = f'{str(number1)} {choice(sign)} {str(number2)}'
    r_answ = get_right_answer(number1, number2, sign)
    return expression, r_answ


def get_right_answer(number1, number2, sign):
    if sign == '+':
        r_answ = str(number1 + number2)
    elif sign == '-':
        r_answ = str(number1 - number2)
    else:
        r_answ = str(number1 * number2)
    return r_answ
