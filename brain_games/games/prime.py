from random import randint
from .. import cli


def game():
    number = randint(1, 100)
    r_answ = is_prime(number)
    answ = cli.question(number)
    if answ == r_answ:
        print('Correct!')
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        return False


def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return 'no'
        return 'yes'
    return 'no'
