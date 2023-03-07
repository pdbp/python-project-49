from random import randint


def game():
    number = randint(1, 100)
    if (number % 2) == 0:
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return number, r_answ


def rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
