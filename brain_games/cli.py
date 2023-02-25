import prompt


def welcome_user(game):
    name = prompt.string('May I have your name? ')
    print(f'hello, {name}!')
    if game == 'brain-calc':
        print('What is the result of the expression?')
    elif game == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain-gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'brain-progression':
        print('What number is missing in the progression?')
    return name


def question(question):
    print(f'Qestion: {question} ')
    answer = prompt.string('Your answer: ')
    return answer
