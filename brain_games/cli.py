import prompt


def welcome_user():
    name = prompt.string('May I have your name????')
    print(f'hello, {name}!')

def even(number):
        answer = prompt.string(f'Qestion: {number} ')
        return answer

def correct():
      print('Correct!')


def wrong():
      print('Wrong')