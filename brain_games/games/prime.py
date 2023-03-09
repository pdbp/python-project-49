from random import randint


def game():
    START_RAND_NUMB_RANGE = 1
    END_RAND_NUMB_RANGE = 100
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    r_answ = is_prime(number)
    return number, r_answ


def is_prime(number):
    if number <= 1:
        return 'no'
    for num in range(2, number):
        if number % num == 0:
            return 'no'
    return 'yes'


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
