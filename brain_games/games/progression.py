from random import randint


def game():
    start_number = randint(1, 100)
    step = randint(1, 5)
    stop_number = start_number + 9 * step
    missing_index = randint(0, 9)
    expression = create_expression(start_number, step, stop_number)
    question = create_question(expression, missing_index)
    r_answ = str(expression[missing_index])
    return question, r_answ


def create_expression(start_number, step, stop_number):
    expression = []
    i = 0
    while start_number + (i * step) <= stop_number:
        expression.append(start_number + step * i)
        i += 1
    return expression


def create_question(expression, missing_index):
    expression_miss = list(expression)
    expression_miss[missing_index] = '..'
    rep_table = str.maketrans('', '', ",[]'")
    return str(expression_miss).translate(rep_table)


def rules():
    return 'What number is missing in the progression?'
