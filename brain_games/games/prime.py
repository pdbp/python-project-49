from random import randint


def game():
    number = randint(1, 100)
    r_answ = is_prime(number)
    return number, r_answ


def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return 'no'
        return 'yes'
    return 'no'


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
