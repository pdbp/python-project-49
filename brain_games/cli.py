import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(question):
    print(f'Question: {question} ')
    answer = prompt.string('Your answer: ')
    return answer
