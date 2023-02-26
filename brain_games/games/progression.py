from random import randint
from .. import cli


def game():
    start_number = randint(1, 100)
    step = randint(1, 5)
    stop_number = start_number + 9 * step
    missing_index = randint(0, 9)
    expression = []
    i = 0
    while start_number + (i * step) <= stop_number:
        expression.append(start_number + step * i)
        i += 1
    r_answ = str(expression[missing_index])
    expression_miss = expression
    expression_miss[missing_index] = '..'
    rep_char = ",[]'"
    new_char = "    "
    rep_table = str.maketrans(rep_char, new_char)
    question = str(expression_miss).translate(rep_table)
    answ = cli.question(question)
    if answ == r_answ:
        print('Correct!')
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{r_answ}'.")
        return False
