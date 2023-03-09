from random import randint


def game():
    START_RAND_NUMB_RANGE = 1
    END_RAND_NUMB_RANGE = 100
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    if (number % 2) == 0:
        r_answ = 'yes'
    else:
        r_answ = 'no'
    return number, r_answ


def rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
