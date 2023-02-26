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
    correct_answer = str(expression[missing_index])
    expression_miss = expression
    expression_miss[missing_index] = '..'
    question = str(expression_miss).replace(',', '').replace('[', '').replace(']', '').replace("'", "")
    answer = cli.question(question)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
