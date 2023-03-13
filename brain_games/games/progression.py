from random import randint
RULES = 'What number is missing in the progression?'
START_RAND_NUMB_RANGE = 1
END_RAND_NUMB_RANGE = 100
START_RAND_STEP_RANGE = 1
END_RAND_STEP_RANGE = 5
AMOUNT_OF_NUMB_IN_PROGRESSION = 10
START_RAND_MISS_IND_RANGE = 0
STOP_RAND_MISS_IND_RANGE = 5


def game():
    start_number = randint(START_RAND_NUMB_RANGE, END_RAND_NUMB_RANGE)
    step = randint(START_RAND_STEP_RANGE, END_RAND_STEP_RANGE)
    stop_number = start_number + (AMOUNT_OF_NUMB_IN_PROGRESSION - 1) * step
    missing_index = randint(START_RAND_MISS_IND_RANGE, STOP_RAND_MISS_IND_RANGE)
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
