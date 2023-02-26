from random import randint
from .. import cli


def game():
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
