from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 100


def game():
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    answer_converter = {True: 'yes', False: 'no'}
    right_answer = answer_converter[is_even(number)]
    return number, right_answer


def is_even(number):
    if (number % 2) == 0:
        right_answer = True
    else:
        right_answer = False
    return right_answer
