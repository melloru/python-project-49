#!/user/bin/env python3
# import sys
# sys.path.insert(0,'/home/eugene/project/python-project-49')
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


def logic(answer, correct_answer, name):
    if str(answer) != str(correct_answer):
        print(f'{answer} is wrong answer ;(. '
              f'Correct answer was {correct_answer}\n'
              f'Lets try again, {name}!')
        return False
    print('Correct!')


if __name__ == '__main__':
    main()
    logic()
# print(sys.path[:])
