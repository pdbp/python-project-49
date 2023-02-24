#!/usr/bin/env python3
from random import randint
from math import gcd
from .. import logic
from .. import cli


def main():
    logic.main('brain-gcd')


def brain_gcd():
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

if __name__ == '__main__':
    main()