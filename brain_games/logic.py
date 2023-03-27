import prompt
CORRECT_ANSWERS_TO_WIN = 3


def run_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    score = 0
    while score < CORRECT_ANSWERS_TO_WIN:
        question, r_ans = game.game()
        print(f'Question: {question} ')
        ans = prompt.string('Your answer: ')
        if ans == r_ans:
            print('Correct!')
            score += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            return 0
    print(f"Congratulations, {name}!")
