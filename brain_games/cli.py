import prompt


def welcome_user(game):
    name = prompt.string('May I have your name? ')
    print(f'hello, {name}!')
    if game == 'brain-calc':
        print('What is the result of the expression?')
    elif game == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def question(question):
    answer = prompt.string(f'Qestion: {question} ')
    return answer
