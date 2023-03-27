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
    right_answer = get_right_answer(number1, number2, sign)
    return expression, right_answer


def get_right_answer(number1, number2, sign):
    if sign == '+':
        right_answer = str(number1 + number2)
    elif sign == '-':
        right_answer = str(number1 - number2)
    else:
        right_answer = str(number1 * number2)
    return right_answer
