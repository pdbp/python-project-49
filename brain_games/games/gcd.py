from random import randint
from math import gcd
from .. import cli


def game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = str(gcd(number1, number2))
    question = str(number1) + ' ' + str(number2)
    answer = cli.question(question)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
