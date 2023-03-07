from . import cli


def main(game):
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(game.rules())
    score = 0
    while score < 3:
        question, r_ans = game.game()
        ans = cli.question(question)
        if ans == r_ans:
            print('Correct!')
            score += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            break
    if score == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
