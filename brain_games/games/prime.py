from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 100


def run_game():
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    answer_converter = {True: 'yes', False: 'no'}
    right_answer = answer_converter[is_prime(number)]
    return number, right_answer


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
