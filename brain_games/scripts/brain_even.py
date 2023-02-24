#!/usr/bin/env python3
from random import randint
from .. import cli
from .. import logic


def main():
    logic.main('brain-even')


def even():
    number = randint(1, 100)
    if (number % 2) == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    answer = cli.question(number)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


if __name__ == '__main__':
    main()
