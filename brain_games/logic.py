from . import cli
from .scripts import brain_calc
from .scripts import brain_even
from .scripts import brain_gcd
from .scripts import brain_progression


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
        return brain_calc.calc()
    elif game == 'brain-even':
        return brain_even.even()
    elif game == 'brain-gcd':
        return brain_gcd.brain_gcd()
    elif game == 'brain-progression':
        return brain_progression.progression()
