from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    START_RAND_NUMB_RANGE = 1
    END_RAND_NUMB_RANGE = 100
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    answer_converter = {True: 'yes', False: 'no'}
    r_answ = answer_converter[is_even(number)]
    return number, r_answ


def is_even(number):
    if (number % 2) == 0:
        r_answ = True
    else:
        r_answ = False
    return r_answ
