from random import randint
from random import choice
RULES = 'What is the result of the expression?'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 25
RAND_SIGNS_RANGE = ('+', '-', '*')


def game():
    number1 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    number2 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    sign = choice(RAND_SIGNS_RANGE)
    expression = f'{number1} {choice(sign)} {number2}'
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
