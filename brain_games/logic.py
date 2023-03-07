from . import cli


def main(game):
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print(game.rules())
    question, r_ans = game.game()
    if is_win(question, r_ans):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def is_win(question, r_ans):
    score = 0
    while score < 3:
        ans = cli.question(question)
        if ans == r_ans:
            print('Correct!')
            score += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            return False
    if score == 3:
        return True
