from random import randint
from math import gcd


def game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    r_answ = str(gcd(number1, number2))
    question = f'{str(number1)} {str(number2)}'
    return question, r_answ


def rules():
    return 'Find the greatest common divisor of given numbers.'
