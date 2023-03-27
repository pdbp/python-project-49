import prompt
CORRECT_ANSWERS_TO_WIN = 3


def run_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    score = 0
    while score < CORRECT_ANSWERS_TO_WIN:
        question, right_answer = game.run_game()
        print(f'Question: {question} ')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            score += 1
        else:
            report_loss(name, answer, right_answer)
            return 0
    print(f"Congratulations, {name}!")


def report_loss(name, reply, right_reply):
    print(f"'{reply}' is wrong answer ;(. Correct answer was '{right_reply}'.")
    print(f"Let's try again, {name}!")
