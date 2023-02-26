from . import cli
from .games import calc
from .games import even
from .games import gcd
from .games import progression
from .games import prime


def main(game):
    print("Welcome to the Brain Games!")
    name = cli.welcome_user(game)
    correct_answers = 0
    while correct_answers < 3:
        if answer(game):
            correct_answers += 1
        else:
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def answer(game):
    if game == 'brain-calc':
        result = calc.game()
    elif game == 'brain-even':
        result = even.game()
    elif game == 'brain-gcd':
        result = gcd.game()
    elif game == 'brain-progression':
        result = progression.game()
    elif game == 'brain-prime':
        result = prime.game()
    return result
