from random import randint
from math import gcd
RULES = 'Find the greatest common divisor of given numbers.'


def game():
    START_RAND_NUMB_RANGE = 1
    END_RAND_NUMB_RANGE = 100
    number1 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    number2 = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    r_answ = str(gcd(number1, number2))
    question = f'{str(number1)} {str(number2)}'
    return question, r_answ
