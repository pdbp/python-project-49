from . import cli


def main(game):
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    CORRECT_ANSWERS_TO_WIN = 3
    print(game.rules())
    score = 0
    while score < CORRECT_ANSWERS_TO_WIN:
        question, r_ans = game.game()
        ans = cli.question(question)
        if ans == r_ans:
            print('Correct!')
            score += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print(f"Let's try again, {name}!")
            return 0
    print(f"Congratulations, {name}!")
