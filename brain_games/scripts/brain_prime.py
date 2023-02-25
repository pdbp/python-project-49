#!usr/bin/env python3
from random import randint
from .. import logic
from .. import cli


def main():
    logic.main('brain-prime')


def prime():
    number = randint(1, 100)
    correct_answer = 'yes'
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                correct_answer = 'no'
                break
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
