#!/usr/bin/env python3
from random import randint
from .. import cli


def main():
    print("Welcome to the Brain Games!")
    cli.welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    working = True
    while working:
        if even():
            correct_answers +=1
            cli.correct()
        else:
            correct_answers = 0
            cli.wrong()

def even():
    number = randint (1, 100)

    if (number % 2) == 0:
        correct_answer = 'yes'
    else: correct_answer = 'no'

    if cli.even(number) == correct_answer:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
