#!/usr/bin/env python3
from random import randint
from random import choice
from .. import cli
from .. import logic


def main():
    logic.main('brain-calc')


def calc():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    seqence = ('+', '-', '*')
    sign = choice(seqence)
    expression = str(number1) + ' ' + choice(sign) + ' ' + str(number2)
    if sign == '+':
        correct_answer = str(number1 + number2)
    elif sign == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)
    answer = cli.question(expression)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'''
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.''')
        return False


if __name__ == '__main__':
    main()
