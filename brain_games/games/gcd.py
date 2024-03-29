from random import randint
from math import gcd
RULES = 'Find the greatest common divisor of given numbers.'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 100


def run_game():
    number1 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    number2 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    right_answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'
    return question, right_answer
