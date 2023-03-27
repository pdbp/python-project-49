from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 100


def run_game():
    number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    print(right_answer)
    return number, right_answer
