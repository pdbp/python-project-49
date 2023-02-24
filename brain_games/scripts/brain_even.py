#!/usr/bin/env python3
from random import randint
from .. import cli


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    working = True
    while working:
        answer = even()
        if answer:
            correct_answers += 1
            if correct_answers == 3:
                print(f"Congratulations, {name}!")
                working = False
        else:
            correct_answers = 0
            print(f"Let's try again, {name}!")
            working = False


def even():
    number = randint(1, 100)
    if (number % 2) == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    answer = cli.even(number)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'''
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.''')
        return False


if __name__ == '__main__':
    main()
